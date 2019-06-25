"""
    Election Services Class
"""
import grpc
from google.protobuf.json_format import MessageToDict
from flask import jsonify, session

from app import db
from app.core import Services

from app.configuration.config import Config

# rpc
from app.rpc import election_pb2
from app.rpc import election_pb2_grpc

class ElectionServices(Services):

    def __init__(self, election_id=None):
        Services.__init__(self)

        self.election_stub = election_pb2_grpc.ElectionStub(self.channel)
        self._token = session["access_token"]
        self.election_id = election_id

    def show_all(self):
        """ return all stored election """
        request = election_pb2.GetElectionsRequest()
        request.header.access_token = self._token
        try:
            result = self.election_stub.GetElections(request)
        except grpc.RpcError as error:
            print(error.code())
            print(error.details())
        # end try
        elections = []
        for election in result.body:
            election = MessageToDict(election, preserving_proto_field_name=True)
            elections.append(election)
        # end for
        return elections
    # end def

    def add(self, request_data):
        # first look up the user in database
        response = {
            "status"  : "success",
            "message" : "successfully added election!"
        }

        request = election_pb2.CreateElectionRequest()
        # header
        request.header.access_token = self._token
        # body
        request.body.name = request_data["name"]
        request.body.description = request_data["description"]

        try:
            result = self.election_stub.CreateElection(request)
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
            "message" : "successfully update election!"
        }

        request = election_pb2.UpdateElectionRequest()
        # header
        request.header.access_token = self._token
        request.header.election_id = self.election_id
        # body
        request.body.name = request_data["name"]
        request.body.description = request_data["description"]

        try:
            result = self.election_stub.UpdateElection(request)
        except grpc.RpcError as error:
            print(error.details())
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try
        return jsonify(response)

    def info(self):
        request = election_pb2.GetElectionRequest()
        request.header.access_token = self._token
        request.header.election_id = self.election_id

        try:
            result = self.election_stub.GetElection(request)
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
            "message" : "successfully remove election!"
        }
        request = election_pb2.RemoveElectionRequest()
        request.header.access_token = self._token
        request.header.election_id = self.election_id

        try:
            result = self.election_stub.RemoveElection(request)
        except grpc.RpcError as error:
            print(error.details())
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try
        return jsonify(response)
