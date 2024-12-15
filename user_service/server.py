from concurrent import futures
import grpc
import UserService_pb2
import UserService_pb2_grpc

# In-memory database for simplicity
users_db = {}

class UserService(UserService_pb2_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        user_id = f"user_{len(users_db) + 1}"
        users_db[user_id] = {
            "name": request.name,
            "email": request.email,
            "password": request.password,
        }
        return UserService_pb2.CreateUserResponse(user_id=user_id, message="User created successfully!")

    def AuthenticateUser(self, request, context):
        for user_id, user in users_db.items():
            if user["email"] == request.email and user["password"] == request.password:
                return UserService_pb2.AuthenticateUserResponse(
                    token="dummy_token_123", message="Authentication successful!"
                )
        return UserService_pb2.AuthenticateUserResponse(
            token="", message="Invalid email or password."
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    UserService_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
