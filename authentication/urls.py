from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import RegisterUserAPIView, UserDetailAPI

urlpatterns = [
    path("user/sign_in", UserDetailAPI.as_view()),
    path("user/sign_up", RegisterUserAPIView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
