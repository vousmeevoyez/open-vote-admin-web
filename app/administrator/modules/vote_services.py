"""
    Vote Result Services Class
"""
import grpc
from google.protobuf.json_format import MessageToDict
from flask import jsonify, session

from app import db

from app.configuration.config import Config

# rpc
from app.rpc import election_pb2
from app.rpc import election_pb2_grpc

class VoteResultServices:

    def __init__(self):
        self.channel = grpc.insecure_channel(Config.GRPC_CHANNEL)
        self.election_stub = election_pb2_grpc.ElectionStub(self.channel)
        self._token = session["access_token"]

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
