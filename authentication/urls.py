from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import RegisterUserAPIView, UserDetailAPI, RestPassword, EditProfile, ForgetPassword, CheckUser

urlpatterns = [
    path("user/sign_in", UserDetailAPI.as_view()),
    path("user/sign_up", RegisterUserAPIView.as_view()),
    path("user/reset_password", RestPassword.as_view()),
    path("user/edit_profile", EditProfile.as_view()),
    path("user/forget_password", ForgetPassword.as_view()),
    path("user/check_user", CheckUser.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
