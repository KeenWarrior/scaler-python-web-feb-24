from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class Profile(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user: User = request.user
        return Response(UserSerializer(user).data)


class UserView(APIView):

    def post(self, request: Request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User(
                username=username
            )
            validate_password(password)
            user.set_password(password)
            user.save()

            return Response(
                UserSerializer(user).data
            )
        except ValidationError as e:
            return Response(
                e.error_list,
                400
            )


