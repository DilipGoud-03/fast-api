import grpc
from concurrent import futures
from grpc_interceptor import ExceptionToStatusInterceptor
from pb.bar_pb2_grpc import add_BarServicer_to_server
from grpc import StatusCode  
from grpc_interceptor.exceptions import NotFound, GrpcException  
from pb.bar_pb2 import OrderResponse  
from pb.bar_pb2_grpc import BarServicer  

mock_drinks = {   
    "soda": 5,
    "beer": 0  
}

class BarService(BarServicer):

    def GetOrder(self, request, context):  
        drinks_stock = mock_drinks.get(request.order)  
        if drinks_stock is None:  
            raise GrpcException(  
                details="Drink not Found",  
                status_code=StatusCode.NOT_FOUND,  
            )
  
        if drinks_stock == 0:  
            raise NotFound(  
                details="Drink out of stock",  
                status_code=StatusCode.NOT_FOUND,  
            )  
  
        return OrderResponse(order_status="Delivery!")


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors)
    add_BarServicer_to_server(BarService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    print('Bar Server Starter...')
    serve()
