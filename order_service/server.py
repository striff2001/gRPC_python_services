from concurrent import futures
import grpc
import OrderService_pb2
import OrderService_pb2_grpc

# In-memory database for simplicity
orders_db = {}

class OrderService(OrderService_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        order_id = f"order_{len(orders_db) + 1}"
        orders_db[order_id] = {
            "user_id": request.user_id,
            "product_ids": list(request.product_ids),
            "status": "created",
        }
        return OrderService_pb2.CreateOrderResponse(order_id=order_id, message="Order created successfully!")

    def GetOrder(self, request, context):
        order = orders_db.get(request.order_id)
        if not order:
            context.abort(grpc.StatusCode.NOT_FOUND, "Order not found")
        return OrderService_pb2.GetOrderResponse(
            order_id=request.order_id,
            user_id=order["user_id"],
            product_ids=order["product_ids"],
            status=order["status"],
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    OrderService_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
