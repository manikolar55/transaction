from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.authtoken.models import Token
from .models import User


class UserDetailAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user_obj = User.objects.get(username=serializer.validated_data["username"])
        if user_obj.password != data["password"]:
            raise ValidationError("Password is incorrect")
        token, created = Token.objects.get_or_create(user=user_obj)
        response = {
            "username": serializer.validated_data["username"],
            "token": token.key,
        }
        return Response(response)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
