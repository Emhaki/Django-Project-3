from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:user_pk>/", views.profile, name="profile"),
    # 카카오 로그인
    path("login/kakao/", views.kakao_request, name="kakao"),
    path("kakao/login/callback/", views.kakao_callback, name="kakao_callback"),
    path("kakao_signup/", views.kakao_signup, name="kakao_signup"),
    # 유효성 검사
    path("send_valid_number/", views.send_valid_number, name="send_valid_number"),
    path("check_valid_number/", views.check_valid_number, name="check_valid_number"),
    # 작가인증
    path("check_artist/", views.check_artist, name="check_artist"),
    path("check_artist_number/", views.check_artist_number, name="check_artist_number"),
]
