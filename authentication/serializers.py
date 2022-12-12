from rest_framework import serializers

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def validate(self, attrs):
        username = attrs["username"]
        password = attrs["password"]
        if not User.objects.filter(email=username):
            raise ValidationError("User email is not correct")
        return attrs

    @property
    def errors(self):
        """
        Returns custom error message

        Returns
        -------
        ReturnDict
            errors dict
        """
        x = super().errors
        if x:
            if x.get("non_field_errors"):
                return {"message": x["non_field_errors"][0], "success": False}
            elif x.get("username"):
                return {"message": "Username field required", "success": False}
            elif x.get("password"):
                return {"message": "Password field required", "success": False}
            return ReturnDict({"errors": x}, serializer=self)
        return ReturnDict(x, serializer=self)


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=True)
    username = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2", "email", "name")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            name=validated_data["name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    @property
    def errors(self):
        """
        Returns custom error message

        Returns
        -------
        ReturnDict
            errors dict
        """
        x = super().errors
        if x:
            if x.get("non_field_errors"):
                return {"message": x["non_field_errors"][0], "success": False}
            elif x.get("username"):
                return {"message": x["username"][0], "success": False}
            elif x.get("password"):
                return {"message": x["password"][0], "success": False}
            elif x.get("name"):
                return {"message": x["name"][0], "success": False}
            elif x.get("email"):
                return {"message": x["email"][0], "success": False}
            elif x.get("password2"):
                return {"message": x["password2"][0], "success": False}
            return ReturnDict({"errors": x}, serializer=self)
        return ReturnDict(x, serializer=self)


class ResetPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=50, required=True)
    new_password = serializers.CharField(max_length=50, required=True)
    again_new_password = serializers.CharField(max_length=50, required=True)

    @property
    def errors(self):
        """
        Returns custom error message

        Returns
        -------
        ReturnDict
            errors dict
        """
        x = super().errors
        if x:
            if x.get("non_field_errors"):
                return {"message": x["non_field_errors"][0], "success": False}
            elif x.get("current_password"):
                return {"message": x["current_password"][0], "success": False}
            elif x.get("new_password"):
                return {"message": x["new_password"][0], "success": False}
            elif x.get("again_new_password"):
                return {"message": x["again_new_password"][0], "success": False}
            return ReturnDict({"errors": x}, serializer=self)
        return ReturnDict(x, serializer=self)


class EditProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=False)
    email = serializers.EmailField(
        required=False, validators=[UniqueValidator(queryset=User.objects.all())]
    )
