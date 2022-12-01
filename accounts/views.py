from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
import requests
from .forms import *
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.


def index(request):
    return render(request, "accounts/index.html")


import secrets, os

state_token = secrets.token_urlsafe(16)
client_id = "064334979be24e5b57f6869948851f37"


def kakao_request(request):
    kakao_api = "https://kauth.kakao.com/oauth/authorize?"
    redirect_uri = "http://localhost:8000/accounts/kakao/login/callback/"

    return redirect(
        f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    )


def kakao_callback(request):
    auth_code = request.GET.get("code")
    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": "http://localhost:8000/accounts/kakao/login/callback/",
        "code": auth_code,
        "client_secret": "dnF1rI5CYOJiylg8ZNfguRTyAMurs2gQ",
    }
    # print(requests.post(kakao_token_api, data=data).json())

    # {
    # 'access_token': 'qq1_knplakFz_KqOTALFuA40U-xEUC_2IqpL3W76Cj10lwAAAYTDOGP9',
    # 'token_type': 'bearer',
    # 'refresh_token': 'gR3DOu7uMp_gipcmR52pbkLkqNqwMWGO6-QDutPtCj10lwAAAYTDOGP8',
    # 'expires_in': 21599, 'scope': 'account_email profile_image profile_nickname',
    # 'refresh_token_expires_in': 5183999
    # }

    temp = requests.post(kakao_token_api, data=data).json()

    access_token = temp["access_token"]
    refresh_token = temp["refresh_token"]
    # print(token_response) # t5Elh2xrH89sIQwsLTkaCrg9ntiOa_68WEzEnuk7CisNIAAAAYTCSQLr
    kakao_user_api = "https://kapi.kakao.com/v2/user/me"
    headers = {"Authorization": f"bearer ${access_token}"}
    user_info_response = requests.get(kakao_user_api, headers=headers).json()
    # print(user_info_response) # <Response [200]>
    # {'id': 2554840000,
    # 'connected_at': '2022-11-29T07:16:11Z',
    # 'properties': {'nickname': '이명학',
    # 'profile_image': 'http://k.kakaocdn.net/dn/sQ8Lg/btrOcfopF8S/39TsSKwP6jBNBEZ5qSikjK/img_640x640.jpg',
    # 'thumbnail_image': 'http://k.kakaocdn.net/dn/sQ8Lg/btrOcfopF8S/39TsSKwP6jBNBEZ5qSikjK/img_110x110.jpg'},
    # 'kakao_account': {'profile_nickname_needs_agreement': False, 'profile_image_needs_agreement': False,
    # 'profile': {'nickname': '이명학', 'thumbnail_image_url': 'http://k.kakaocdn.net/dn/sQ8Lg/btrOcfopF8S/39TsSKwP6jBNBEZ5qSikjK/img_110x110.jpg', 'profile_image_url': 'http://k.kakaocdn.net/dn/sQ8Lg/btrOcfopF8S/39TsSKwP6jBNBEZ5qSikjK/img_640x640.jpg',
    # 'is_default_image': False}, 'has_email': True, 'email_needs_agreement': False, 'is_email_valid': True, 'is_email_verified': True, 'email': 'mhmh779@naver.com'}
    # }

    kakao_id = user_info_response["id"]
    kakao_nickname = user_info_response["properties"]["nickname"]
    kakao_email = (
        user_info_response["kakao_account"].get("email")
        if "email" in user_info_response["kakao_account"]
        else ""
    )
    kakao_profile_image = user_info_response["properties"]["profile_image"]

    if get_user_model().objects.filter(username=kakao_id).exists():
        kakao_user = get_user_model().objects.get(username=kakao_id)
        kakao_user.profileimage = kakao_profile_image
        kakao_user.refresh_token = refresh_token
        kakao_user.save()
    else:
        kakao_login_user = get_user_model().objects.create(
            username=kakao_id,
            nickname=kakao_nickname,
            profileimage=kakao_profile_image,
            email=kakao_email,
            refresh_token=refresh_token,
        )
        kakao_login_user.set_password(str(state_token))
        kakao_login_user.save()
        kakao_user = get_user_model().objects.get(username=kakao_id)

    auth_login(request, kakao_user)
    return redirect("accounts:index")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.save()
            return redirect("accounts:login")
    else:
        return render(request, "accounts/signup.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:index")
