"""
    Auth Services
    _________________
"""
import grpc
import jwt
from sqlalchemy.exc import IntegrityError
from flask import jsonify, session

from app.configuration.config import Config
# rpc
from app.rpc import auth_pb2
from app.rpc import auth_pb2_grpc
from app.rpc import user_pb2 
from app.rpc import user_pb2_grpc

class AuthServices:

    def __init__(self):
        self.channel = grpc.insecure_channel(Config.GRPC_CHANNEL)
        self.auth_stub = auth_pb2_grpc.AuthStub(self.channel)
        self.user_stub = user_pb2_grpc.UserStub(self.channel)
    # end def

    def login(self, request_data):
        response = {
            "status"  : "success",
            "message" : "successfully logged in!",
            "redirect" : None
        }

        # call RPC
        request = auth_pb2.AccessTokenRequest()
        request.username = request_data["username"]
        request.password = request_data["password"]
        try:
            result = self.auth_stub.GetAccessToken(request)
        except grpc.RpcError as error:
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try

        token = result.body.access_token
        token_payload = jwt.decode(token, Config.JWT_SECRET, algorithm="HS256")
        user_id = token_payload["sub"]

        # decode user id and get user information
        request = user_pb2.GetUserRequest()
        request.header.access_token = token
        request.header.user_id = user_id
        try:
            result = self.user_stub.GetUser(request)
            user = result.body
        except grpc.RpcError as error:
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try

        session['username'] = user.username
        session['access_token'] = token

        # set redirect url
        response["redirect"] = "/admin/users"
        return jsonify(response)
    # end def
