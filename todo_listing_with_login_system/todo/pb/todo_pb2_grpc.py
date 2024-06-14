# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import pb.todo_pb2 as todo__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in todo_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TodoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTodo = channel.unary_unary(
                '/todos.TodoService/CreateTodo',
                request_serializer=todo__pb2.CreateTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.CreateTodoResponse.FromString,
                _registered_method=True)
        self.GetTodo = channel.unary_unary(
                '/todos.TodoService/GetTodo',
                request_serializer=todo__pb2.GetTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.GetTodoResponse.FromString,
                _registered_method=True)
        self.DeleteTodo = channel.unary_unary(
                '/todos.TodoService/DeleteTodo',
                request_serializer=todo__pb2.DeleteTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.DeleteTodoResponse.FromString,
                _registered_method=True)
        self.UpdateTodo = channel.unary_unary(
                '/todos.TodoService/UpdateTodo',
                request_serializer=todo__pb2.UpdateTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.UpdateTodoResponse.FromString,
                _registered_method=True)
        self.CreateComment = channel.unary_unary(
                '/todos.TodoService/CreateComment',
                request_serializer=todo__pb2.CreateCommentRequest.SerializeToString,
                response_deserializer=todo__pb2.CreateCommentResponse.FromString,
                _registered_method=True)
        self.GetComments = channel.unary_unary(
                '/todos.TodoService/GetComments',
                request_serializer=todo__pb2.GetCommentsRequest.SerializeToString,
                response_deserializer=todo__pb2.GetCommentsResponse.FromString,
                _registered_method=True)


class TodoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetComments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTodo,
                    request_deserializer=todo__pb2.CreateTodoRequest.FromString,
                    response_serializer=todo__pb2.CreateTodoResponse.SerializeToString,
            ),
            'GetTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodo,
                    request_deserializer=todo__pb2.GetTodoRequest.FromString,
                    response_serializer=todo__pb2.GetTodoResponse.SerializeToString,
            ),
            'DeleteTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTodo,
                    request_deserializer=todo__pb2.DeleteTodoRequest.FromString,
                    response_serializer=todo__pb2.DeleteTodoResponse.SerializeToString,
            ),
            'UpdateTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTodo,
                    request_deserializer=todo__pb2.UpdateTodoRequest.FromString,
                    response_serializer=todo__pb2.UpdateTodoResponse.SerializeToString,
            ),
            'CreateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateComment,
                    request_deserializer=todo__pb2.CreateCommentRequest.FromString,
                    response_serializer=todo__pb2.CreateCommentResponse.SerializeToString,
            ),
            'GetComments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetComments,
                    request_deserializer=todo__pb2.GetCommentsRequest.FromString,
                    response_serializer=todo__pb2.GetCommentsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todos.TodoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('todos.TodoService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TodoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todos.TodoService/CreateTodo',
            todo__pb2.CreateTodoRequest.SerializeToString,
            todo__pb2.CreateTodoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todos.TodoService/GetTodo',
            todo__pb2.GetTodoRequest.SerializeToString,
            todo__pb2.GetTodoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todos.TodoService/DeleteTodo',
            todo__pb2.DeleteTodoRequest.SerializeToString,
            todo__pb2.DeleteTodoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todos.TodoService/UpdateTodo',
            todo__pb2.UpdateTodoRequest.SerializeToString,
            todo__pb2.UpdateTodoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todos.TodoService/CreateComment',
            todo__pb2.CreateCommentRequest.SerializeToString,
            todo__pb2.CreateCommentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetComments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todos.TodoService/GetComments',
            todo__pb2.GetCommentsRequest.SerializeToString,
            todo__pb2.GetCommentsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
