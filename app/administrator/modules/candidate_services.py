"""
    Candidates Services Class
"""
import grpc
from google.protobuf.json_format import MessageToDict
from flask import jsonify, session

from app import db

from app.configuration.config import Config

# rpc
from app.rpc import candidate_pb2
from app.rpc import candidate_pb2_grpc

class CandidateServices:

    def __init__(self, candidate_id=None, election_id=None):
        self.channel = grpc.insecure_channel(Config.GRPC_CHANNEL)
        self.candidate_stub = candidate_pb2_grpc.CandidateStub(self.channel)
        self._token = session["access_token"]
        self.election_id = election_id
        self.candidate_id = candidate_id

    def show_all(self):
        """ return all stored election """
        request = candidate_pb2.GetCandidatesRequest()
        request.header.access_token = self._token
        request.header.election_id = self.election_id
        try:
            result = self.candidate_stub.GetCandidates(request)
        except grpc.RpcError as error:
            print(error.code())
            print(error.details())
        # end try
        candidates = []
        for candidate in result.body:
            candidate = MessageToDict(candidate, preserving_proto_field_name=True)
            candidates.append(candidate)
        # end for
        return candidates
    # end def

    def add(self, request_data):
        # first look up the user in database
        response = {
            "status"  : "success",
            "message" : "successfully added candidate!"
        }

        request = candidate_pb2.CreateCandidateRequest()
        # header
        request.header.access_token = self._token
        request.header.election_id = self.election_id
        # body
        request.body.name = request_data["name"]
        request.body.description = request_data["description"]
        request.body.order_no = request_data["order_no"]

        try:
            result = self.candidate_stub.CreateCandidate(request)
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
            "message" : "successfully update candidate!"
        }

        request = candidate_pb2.UpdateCandidateRequest()
        # header
        request.header.access_token = self._token
        request.header.candidate_id = self.candidate_id
        request.header.election_id = self.election_id
        # body
        request.body.name = request_data["name"]
        request.body.description = request_data["description"]
        request.body.order_no = request_data["order_no"]

        try:
            result = self.candidate_stub.UpdateCandidate(request)
        except grpc.RpcError as error:
            print(error.details())
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try
        return jsonify(response)

    def info(self):
        request = candidate_pb2.GetCandidateRequest()
        request.header.access_token = self._token
        request.header.election_id = self.election_id
        request.header.candidate_id = self.candidate_id

        try:
            result = self.candidate_stub.GetCandidate(request)
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
        request = candidate_pb2.RemoveCandidateRequest()
        request.header.access_token = self._token
        request.header.election_id = self.election_id
        request.header.candidate_id = self.candidate_id

        try:
            result = self.candidate_stub.RemoveCandidate(request)
        except grpc.RpcError as error:
            print(error.details())
            response["status"] = "failed"
            response["message"] = error.details()
            return jsonify(response)
        # end try
        return jsonify(response)
