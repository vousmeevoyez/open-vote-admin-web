"""
    User Services Class
"""
import grpc
from google.protobuf.json_format import MessageToDict
from flask import jsonify, session

from app import db
from app.core import Services

from app.configuration.config import Config

# rpc
from app.rpc import user_pb2
from app.rpc import user_pb2_grpc

class UserServices(Services):

    def __init__(self, user_id=None):
        Services.__init__(self)

        self.user_stub = user_pb2_grpc.UserStub(self.channel)
        self._token = session["access_token"]
        self.user_id = user_id

    def show_all(self):
        """ return all stored user """
        request = user_pb2.GetUsersRequest()
        request.header.access_token = self._token
        try:
            result = self.user_stub.GetUsers(request)
        except grpc.RpcError as error:
            print(error.code())
            print(error.details())
        # end try
        users = []
        for user in result.body:
            user = MessageToDict(user, preserving_proto_field_name=True)
            users.append(user)
        # end for
        return users
    # end def

    def add(self, request_data):
        # first look up the user in database
        response = {
            "status"  : "success",
            "message" : "successfully added user!"
        }

        request = user_pb2.CreateUserRequest()
        # header
        request.header.access_token = self._token
        # body
        request.body.username = request_data["username"]
        request.body.name = request_data["name"]
        request.body.identity_id = request_data["identity_id"]
        request.body.msisdn = request_data["msisdn"]
        request.body.email = request_data["email"]
        request.body.role = request_data["role"]
        request.body.password = request_data["password"]

        try:
            result = self.user_stub.CreateUser(request)
        except grpc.RpcError as error:
            print(error.details())
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try
        return jsonify(response)

    def update(self, request_data):
        # first look up the user in database
        response = {
            "status"  : "success",
            "message" : "successfully update user!"
        }

        request = user_pb2.UpdateUserRequest()
        # header
        request.header.access_token = self._token
        request.header.user_id = self.user_id
        # body
        request.body.name = request_data["name"]
        request.body.identity_id = request_data["identity_id"]
        request.body.msisdn = request_data["msisdn"]
        request.body.email = request_data["email"]
        request.body.role = request_data["role"]
        request.body.password = request_data["password"]

        try:
            result = self.user_stub.UpdateUser(request)
        except grpc.RpcError as error:
            print(error.details())
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try
        return jsonify(response)

    def info(self):
        request = user_pb2.GetUserRequest()
        request.header.access_token = self._token
        request.header.user_id = self.user_id

        try:
            result = self.user_stub.GetUser(request)
        except grpc.RpcError as error:
            print(error.details())
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try
        response = MessageToDict(result.body, preserving_proto_field_name=True)
        return jsonify(response)

    def remove(self):
        response = {
            "status"  : "success",
            "message" : "successfully remove user!"
        }
        request = user_pb2.RemoveUserRequest()
        request.header.access_token = self._token
        request.header.user_id = self.user_id

        try:
            result = self.user_stub.RemoveUser(request)
        except grpc.RpcError as error:
            print(error.details())
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try

        return jsonify(response)

    def enroll(self, candidate_id):
        response = {
            "status"  : "success",
            "message" : "successfully enroll user!"
        }
        request = user_pb2.EnrollUserRequest()
        request.header.access_token = self._token
        request.header.user_id = self.user_id
        request.header.candidate_id = candidate_id

        try:
            result = self.user_stub.EnrollUser(request)
        except grpc.RpcError as error:
            print(error.details())
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try

        return jsonify(response)
