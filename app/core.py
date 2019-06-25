"""
    Core Class
"""
import os
from pathlib import Path

import grpc
from flask import current_app

from app.configuration.config import Config

class Services:

    def __init__(self):
        self.channel = None
        self._setup_rpc(self._load_certificate())

    def _load_certificate(self):
        """ load certificate and return it"""
        certificate = os.environ.get("CERTIFICATE", None)
        if certificate is None:
            return None

        full_path = os.path.join(self._get_root_path(), certificate)
        with open(full_path, "rb") as file_:
            certificate = file_.read()

        credentials = \
        grpc.ssl_channel_credentials(root_certificates=certificate)
        return credentials
	# end def

    def _get_root_path(self):
        return current_app.root_path

    def _setup_rpc(self, credentials=None):
        if credentials is None:
            self.channel = grpc.insecure_channel(Config.GRPC_CHANNEL)
        else:
            self.channel = grpc.secure_channel(Config.GRPC_CHANNEL, credentials)
