from dependency_injector.wiring import inject, Provide
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from d_injector_demo.services import UserService


class CreateListUserView(APIView):
    user_service: UserService

    @inject
    def __init__(
            self,
            user_service: UserService = Provide["user_service"]
    ):
        super().__init__()
        self.user_service = user_service

    def post(self, request: Request):
        user = self.user_service.create_user(request.data["name"], request.data["email"])
        return Response(
            {
                "name": user.name,
                "email": user.email
            }
        )
