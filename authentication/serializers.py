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
            if x.get('non_field_errors'):
                return {'message': x['non_field_errors'][0], 'success': False}
            elif x.get('username'):
                return {'message': "Username field required", 'success': False}
            elif x.get('password'):
                return {'message': "Password field required", 'success': False}
            return ReturnDict({'errors': x}, serializer=self)
        return ReturnDict(x, serializer=self)


class RegisterSerializer(serializers.ModelSerializer):
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
