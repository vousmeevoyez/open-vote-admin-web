# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import app.rpc.user_pb2 as user__pb2


class UserStub(object):
  """user service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateUser = channel.unary_unary(
        '/User/CreateUser',
        request_serializer=user__pb2.CreateUserRequest.SerializeToString,
        response_deserializer=user__pb2.CreateUserResponse.FromString,
        )
    self.GetUser = channel.unary_unary(
        '/User/GetUser',
        request_serializer=user__pb2.GetUserRequest.SerializeToString,
        response_deserializer=user__pb2.GetUserResponse.FromString,
        )
    self.UpdateUser = channel.unary_unary(
        '/User/UpdateUser',
        request_serializer=user__pb2.UpdateUserRequest.SerializeToString,
        response_deserializer=user__pb2.UpdateUserResponse.FromString,
        )
    self.RemoveUser = channel.unary_unary(
        '/User/RemoveUser',
        request_serializer=user__pb2.RemoveUserRequest.SerializeToString,
        response_deserializer=user__pb2.RemoveUserResponse.FromString,
        )
    self.GetUsers = channel.unary_unary(
        '/User/GetUsers',
        request_serializer=user__pb2.GetUsersRequest.SerializeToString,
        response_deserializer=user__pb2.GetUsersResponse.FromString,
        )
    self.EnrollUser = channel.unary_unary(
        '/User/EnrollUser',
        request_serializer=user__pb2.EnrollUserRequest.SerializeToString,
        response_deserializer=user__pb2.EnrollUserResponse.FromString,
        )
    self.UnrollUser = channel.unary_unary(
        '/User/UnrollUser',
        request_serializer=user__pb2.UnrollUserRequest.SerializeToString,
        response_deserializer=user__pb2.UnrollUserResponse.FromString,
        )


class UserServicer(object):
  """user service definition
  """

  def CreateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUsers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EnrollUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnrollUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=user__pb2.CreateUserRequest.FromString,
          response_serializer=user__pb2.CreateUserResponse.SerializeToString,
      ),
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=user__pb2.GetUserRequest.FromString,
          response_serializer=user__pb2.GetUserResponse.SerializeToString,
      ),
      'UpdateUser': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateUser,
          request_deserializer=user__pb2.UpdateUserRequest.FromString,
          response_serializer=user__pb2.UpdateUserResponse.SerializeToString,
      ),
      'RemoveUser': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveUser,
          request_deserializer=user__pb2.RemoveUserRequest.FromString,
          response_serializer=user__pb2.RemoveUserResponse.SerializeToString,
      ),
      'GetUsers': grpc.unary_unary_rpc_method_handler(
          servicer.GetUsers,
          request_deserializer=user__pb2.GetUsersRequest.FromString,
          response_serializer=user__pb2.GetUsersResponse.SerializeToString,
      ),
      'EnrollUser': grpc.unary_unary_rpc_method_handler(
          servicer.EnrollUser,
          request_deserializer=user__pb2.EnrollUserRequest.FromString,
          response_serializer=user__pb2.EnrollUserResponse.SerializeToString,
      ),
      'UnrollUser': grpc.unary_unary_rpc_method_handler(
          servicer.UnrollUser,
          request_deserializer=user__pb2.UnrollUserRequest.FromString,
          response_serializer=user__pb2.UnrollUserResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'User', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
