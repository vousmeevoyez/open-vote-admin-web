# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nauth.proto\"8\n\x12\x41\x63\x63\x65ssTokenRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\\\n\x13\x41\x63\x63\x65ssTokenResponse\x12\'\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x19.AccessTokenResponse.Body\x1a\x1c\n\x04\x42ody\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\"0\n\x18RevokeAccessTokenRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\"+\n\x19RevokeAccessTokenResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\x93\x01\n\x04\x41uth\x12=\n\x0eGetAccessToken\x12\x13.AccessTokenRequest\x1a\x14.AccessTokenResponse\"\x00\x12L\n\x11RevokeAccessToken\x12\x19.RevokeAccessTokenRequest\x1a\x1a.RevokeAccessTokenResponse\"\x00\x62\x06proto3')
)




_ACCESSTOKENREQUEST = _descriptor.Descriptor(
  name='AccessTokenRequest',
  full_name='AccessTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='AccessTokenRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='AccessTokenRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=70,
)


_ACCESSTOKENRESPONSE_BODY = _descriptor.Descriptor(
  name='Body',
  full_name='AccessTokenResponse.Body',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='AccessTokenResponse.Body.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=164,
)

_ACCESSTOKENRESPONSE = _descriptor.Descriptor(
  name='AccessTokenResponse',
  full_name='AccessTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='AccessTokenResponse.body', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ACCESSTOKENRESPONSE_BODY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=164,
)


_REVOKEACCESSTOKENREQUEST = _descriptor.Descriptor(
  name='RevokeAccessTokenRequest',
  full_name='RevokeAccessTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='RevokeAccessTokenRequest.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=214,
)


_REVOKEACCESSTOKENRESPONSE = _descriptor.Descriptor(
  name='RevokeAccessTokenResponse',
  full_name='RevokeAccessTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='RevokeAccessTokenResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=259,
)

_ACCESSTOKENRESPONSE_BODY.containing_type = _ACCESSTOKENRESPONSE
_ACCESSTOKENRESPONSE.fields_by_name['body'].message_type = _ACCESSTOKENRESPONSE_BODY
DESCRIPTOR.message_types_by_name['AccessTokenRequest'] = _ACCESSTOKENREQUEST
DESCRIPTOR.message_types_by_name['AccessTokenResponse'] = _ACCESSTOKENRESPONSE
DESCRIPTOR.message_types_by_name['RevokeAccessTokenRequest'] = _REVOKEACCESSTOKENREQUEST
DESCRIPTOR.message_types_by_name['RevokeAccessTokenResponse'] = _REVOKEACCESSTOKENRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessTokenRequest = _reflection.GeneratedProtocolMessageType('AccessTokenRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACCESSTOKENREQUEST,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:AccessTokenRequest)
  ))
_sym_db.RegisterMessage(AccessTokenRequest)

AccessTokenResponse = _reflection.GeneratedProtocolMessageType('AccessTokenResponse', (_message.Message,), dict(

  Body = _reflection.GeneratedProtocolMessageType('Body', (_message.Message,), dict(
    DESCRIPTOR = _ACCESSTOKENRESPONSE_BODY,
    __module__ = 'auth_pb2'
    # @@protoc_insertion_point(class_scope:AccessTokenResponse.Body)
    ))
  ,
  DESCRIPTOR = _ACCESSTOKENRESPONSE,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:AccessTokenResponse)
  ))
_sym_db.RegisterMessage(AccessTokenResponse)
_sym_db.RegisterMessage(AccessTokenResponse.Body)

RevokeAccessTokenRequest = _reflection.GeneratedProtocolMessageType('RevokeAccessTokenRequest', (_message.Message,), dict(
  DESCRIPTOR = _REVOKEACCESSTOKENREQUEST,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:RevokeAccessTokenRequest)
  ))
_sym_db.RegisterMessage(RevokeAccessTokenRequest)

RevokeAccessTokenResponse = _reflection.GeneratedProtocolMessageType('RevokeAccessTokenResponse', (_message.Message,), dict(
  DESCRIPTOR = _REVOKEACCESSTOKENRESPONSE,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:RevokeAccessTokenResponse)
  ))
_sym_db.RegisterMessage(RevokeAccessTokenResponse)



_AUTH = _descriptor.ServiceDescriptor(
  name='Auth',
  full_name='Auth',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=262,
  serialized_end=409,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAccessToken',
    full_name='Auth.GetAccessToken',
    index=0,
    containing_service=None,
    input_type=_ACCESSTOKENREQUEST,
    output_type=_ACCESSTOKENRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RevokeAccessToken',
    full_name='Auth.RevokeAccessToken',
    index=1,
    containing_service=None,
    input_type=_REVOKEACCESSTOKENREQUEST,
    output_type=_REVOKEACCESSTOKENRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTH)

DESCRIPTOR.services_by_name['Auth'] = _AUTH

# @@protoc_insertion_point(module_scope)
