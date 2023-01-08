from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, ResetPasswordSerializer, EditProfileSerializer
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
        user_obj = User.objects.get(email=serializer.validated_data["username"])
        if user_obj.password != data["password"]:
            res = {'message': "password is incorrect", 'success': False}
            return Response(res)
        token, created = Token.objects.get_or_create(user=user_obj)
        response = {
            "name": user_obj.name,
            "username": serializer.validated_data["username"],
            "token": token.key,
        }
        return Response(response)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class RestPassword(APIView):
    def post(self, request):
        data = request.data
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = User.objects.filter(id=request.user.id).first()
        if user_data:
            if user_data.password == data["current_password"]:
                if data["new_password"] == data["again_new_password"]:
                    user_data.password = data["new_password"]
                    user_data.save(update_fields=["password"])
                    return Response("Password Changed", status=200)
                else:
                    return Response("Password Not Matched", status=200)
            else:
                return Response("Enter Correct Password", status=200)
        else:
            return Response("User Not Found", status=200)


class EditProfile(APIView):
    def put(self, request):
        data = request.data
        serializer = EditProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = User.objects.filter(email=request.user.email).first()
        if user_data:
            try:
                if data["name"]:
                    user_data.name = data["name"]
                    user_data.save(update_fields=["name"])
                    return Response("Name Updated", status=200)
            except:
                if data["email"]:
                    user_data.email = data["email"]
                    user_data.username = data["email"]
                    user_data.save(update_fields=["email", "username"])
                    return Response("Email Updated", status=200)
        else:
            return Response("User Not Found", status=200)
