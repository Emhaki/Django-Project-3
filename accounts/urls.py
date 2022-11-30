from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("login/kakao/", views.kakao_request, name="kakao"),
    path("kakao/login/callback/", views.kakao_callback, name="kakao_callback"),
    path("send_valid_number/", views.send_valid_number, name="send_valid_number"),
    path("check_valid_number/", views.check_valid_number, name="check_valid_number"),
]
