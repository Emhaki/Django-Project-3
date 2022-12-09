from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
import requests
from django.contrib import messages
from random import random
from .forms import *
from articles .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
import json
from django.core.mail import EmailMessage
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

    # 이메일 동의 안할시 공백을 주었음
    kakao_id = user_info_response["id"]
    kakao_nickname = user_info_response["properties"]["nickname"]
    kakao_email = (
        user_info_response["kakao_account"].get("email")
        if "email" in user_info_response["kakao_account"]
        else ""
    )
    kakao_profile_image = user_info_response["properties"]["profile_image"]

    if get_user_model().objects.filter(test=kakao_id).exists():
        kakao_user = get_user_model().objects.get(test=kakao_id)
        kakao_user.profileimage = kakao_profile_image
        kakao_user.refresh_token = refresh_token
        kakao_user.save()
        auth_login(request, kakao_user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("accounts:profile", request.user.pk)
    else:
        kakao_login_user = get_user_model().objects.create(
            test=kakao_id,
            nickname=kakao_nickname,
            profileimage=kakao_profile_image,
            email=kakao_email,
            refresh_token=refresh_token,
        )
        kakao_login_user.set_password(str(state_token))
        kakao_login_user.save()
        kakao_user = get_user_model().objects.get(test=kakao_id)
        auth_login(request, kakao_user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("accounts:kakao_signup")


def kakao_signup(request):
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
              form.save()
              return redirect("accounts:profile", request.user.pk)
    else:
        if request.GET:
          names = get_user_model().objects.filter(username=request.GET.get("username"))
          if names:
            context = {
              'check' : "True",
            }
            return JsonResponse(context)
          else:
            context = {
              'check' : "False",
            }
            return JsonResponse(context)
    return render(request, "accounts/kakao_signup.html")

def signup(request):

    if request.method == "POST":
      form = SignupForm(request.POST)
      if form.is_valid():
        forms = form.save(commit=False)
        forms.email = request.POST.get('email')
        forms.save()
        return redirect("accounts:login")
    else:
      if request.GET:
        names = get_user_model().objects.filter(username=request.GET.get("username"))
        if names:
          context = {
            'check' : "True",
          }
          return JsonResponse(context)
        else:
          context = {
            'check' : "False",
          }
          return JsonResponse(context)
    return render(request, "accounts/signup.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    auth_logout(request)
    return redirect("accounts:login")

def social(request):

    if request.method == "POST":
        form = UpdateSocialForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile", request.user.pk)

    return render(request, "accounts/social_update.html")

# 
def profile(request, user_pk):
    profiles = get_user_model().objects.filter(pk=user_pk)
    creater = get_user_model().objects.filter(pk=user_pk).filter(is_creater=1)
    # 작가가 등록한 작품들
    arts = Art.objects.filter(artist=user_pk).order_by()
    paginator = Paginator(arts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # 해당 유저가 좋아요를 누른 작품들
    art_likes = Art.objects.filter(likes=user_pk).filter().order_by()
    like_paginator = Paginator(art_likes, 6)
    page_number = request.GET.get("like_page")
    like_page_obj = like_paginator.get_page(page_number)

    context = {
      "profiles" : profiles,
      "creater": creater,
      "arts" : arts,
      "art_likes": art_likes,
      "page_obj": page_obj,
      "like_page_obj": like_page_obj,
    }
    return render(request, "accounts/profile.html", context)


# 이메일 인증
def send_valid_number(request):
    validnumber = round(random() * 10000)
    print(f"{validnumber} 유효성 번호")
    current_site = get_current_site(request)
    message = render_to_string(
        "accounts/send_valid_number.html",
        {
            "user": request.user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(request.user.pk))
            .encode()
            .decode(),
            "validnumber": validnumber,
        },
    )

    mail_subject = "[NES]이메일 인증번호입니다."
    user_email = json.loads(request.body)["user_email"]
    email = EmailMessage(mail_subject, message, to=[user_email])
    email.send()

    return JsonResponse({"validnumber": validnumber})


def check_valid_number(request):
    valid_number = json.loads(request.body)["valid_number"]
    input_number = json.loads(request.body)["input_number"]
    print(json.loads(request.body))
    print(valid_number, input_number)
    if valid_number == input_number:
        check = True
    else:
        check = False
    return JsonResponse({"check": check})


# 작가 인증
def check_artist(request):
    validnumber = round(random() * 10000)
    print(f"{validnumber} 유효성 번호")
    current_site = get_current_site(request)
    message = render_to_string(
        "accounts/check_artist.html",
        {
            "user": request.user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(request.user.pk))
            .encode()
            .decode(),
            "validnumber": validnumber,
        },
    )

    mail_subject = "[NES]이메일 인증번호입니다."
    user_email = json.loads(request.body)["user_email"]
    if "ac.kr" in user_email[:] or "edu" in user_email[-4:]:
        email = EmailMessage(mail_subject, message, to=[user_email])
        email.send()
        return JsonResponse({"validnumber": validnumber})
    else:
        messages(request, "학교 이메일이 아니에요.")
        return redirect("profile")


def check_artist_number(request):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    valid_number = json.loads(request.body)["valid_number"]
    input_number = json.loads(request.body)["input_number"]
    print(user)
    if valid_number == input_number:
        check = True
        user.is_creater = True
        user.save()
    else:
        check = False
    return JsonResponse({"check": check,})