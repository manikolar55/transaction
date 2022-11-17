from django.urls import path
from .views import RegisterUserAPIView, UserDetailAPI

urlpatterns = [
    path("user/sign_in", UserDetailAPI.as_view()),
    path("user/sign_up", RegisterUserAPIView.as_view()),
]
