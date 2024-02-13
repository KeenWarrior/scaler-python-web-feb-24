from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from ..models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from ..serializers import UserSerializer


class CreateGetAllUsersView(APIView):
    def get(self, request):

        users = User.objects.filter()

        serialized = UserSerializer(users, many=True)

        return Response(
            serialized.data, 200
        )

    def post(self, request: Request):

        serialized = UserSerializer(data=request.data)

        if not serialized.is_valid():
            return Response(serialized.errors, 400)

        serialized.save()

        return Response(
            serialized.data, 201
        )


class GetUpdateDeleteUserView(APIView):

    def get(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)

        serialized = UserSerializer(user)
        return Response(
            serialized.data, 200
        )

    def put(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)

        serialized = UserSerializer(data=request.data)

        if not serialized.is_valid():
            return Response(
                serialized.errors, 400
            )

        user.name = serialized.data["name"]
        user.email = serialized.data["email"]
        user.save()

        updated_serialized = UserSerializer(user)

        return Response(
            updated_serialized.data, 200
        )

    def delete(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        serialized = UserSerializer(user)
        user.delete()

        return Response({
            serialized.data
        }, 200)



