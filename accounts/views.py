from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
import requests
from django.http import JsonResponse

# Create your views here.

def index(request):
  return render(request, "accounts/index.html")

def signup(request):

  return render(request, "accounts/signup.html")

def login(request):

  return render(request, "accounts/login.html")

import secrets, os
state_token = secrets.token_urlsafe(16)
client_id = "064334979be24e5b57f6869948851f37"

def kakao_request(request):
    kakao_api = "https://kauth.kakao.com/oauth/authorize?"
    redirect_uri = "http://localhost:8000/accounts/kakao/login/callback/"

    return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")


def kakao_callback(request):
    auth_code = request.GET.get('code')
    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": "http://localhost:8000/accounts/kakao/login/callback/",
        "code": auth_code,
        "client_secret": "dnF1rI5CYOJiylg8ZNfguRTyAMurs2gQ",
    }
    # {
    # "token": 
    #   {
    #     "access_token": "A5JWDyT4N9e6RANqDmsZOixfMFMKrPRlzQLrTObRCilvVQAAAYTCPkRK",
    #     "token_type": "bearer", 
    #     "refresh_token": "i4SFulIhZdkcrzGjZAr5mCxlkzIarnABLhNfI2JzCilvVQAAAYTCPkRJ",
    #     "expires_in": 21599, 
    #     "scope": "account_email profile_nickname", 
    #     "refresh_token_expires_in": 5183999
    #   }
    # }
    
    token_response = requests.post(kakao_token_api, data=data).json()['access_token']
    # refresh_token = requests.post(kakao_token_api, data=data).json()['refresh_token']
    print(token_response) # t5Elh2xrH89sIQwsLTkaCrg9ntiOa_68WEzEnuk7CisNIAAAAYTCSQLr
    access_token = token_response
    kakao_user_api = "https://kapi.kakao.com/v2/user/me"
    headers = {"Authorization": f"bearer ${access_token}"}
    user_info_response = requests.get(kakao_user_api, headers=headers)
    print(user_info_response) # <Response [200]>
    print(user_info_response.json())

    # {'id': 2554840000,
    # 'connected_at': '2022-11-29T07:16:11Z', 
    # 'properties': {'nickname': '이명학', 
    # 'profile_image': 'http://k.kakaocdn.net/dn/sQ8Lg/btrOcfopF8S/39TsSKwP6jBNBEZ5qSikjK/img_640x640.jpg', 
    # 'thumbnail_image': 'http://k.kakaocdn.net/dn/sQ8Lg/btrOcfopF8S/39TsSKwP6jBNBEZ5qSikjK/img_110x110.jpg'}, 
    # 'kakao_account': {'profile_nickname_needs_agreement': False, 'profile_image_needs_agreement': False, 
    # 'profile': {'nickname': '이명학', 'thumbnail_image_url': 'http://k.kakaocdn.net/dn/sQ8Lg/btrOcfopF8S/39TsSKwP6jBNBEZ5qSikjK/img_110x110.jpg', 'profile_image_url': 'http://k.kakaocdn.net/dn/sQ8Lg/btrOcfopF8S/39TsSKwP6jBNBEZ5qSikjK/img_640x640.jpg', 
    # 'is_default_image': False}, 'has_email': True, 'email_needs_agreement': False, 'is_email_valid': True, 'is_email_verified': True, 'email': 'mhmh779@naver.com'}
    # }

    kakao_id = user_info_response.json()['id']
    kakao_nickname = user_info_response.json()['properties']['nickname']
    kakao_email = user_info_response.json()['kakao_account'].get("email")
    kakao_profile_image = user_info_response.json()["properties"]["profile_image"]

    if get_user_model().objects.filter(username=kakao_id).exists():
      kakao_user = get_user_model().objects.get(username=kakao_id)
      kakao_user.profileimage = kakao_profile_image
      # kakao_user.refresh_token = refresh_token
      kakao_user.save()
    else:
      kakao_login_user = get_user_model().objects.create(
        username = kakao_id,
        nickname = kakao_nickname,
        profileimage=kakao_profile_image,
        email = kakao_email,
        # refresh_token = refresh_token
      )
      kakao_login_user.set_password(str(state_token))
      kakao_login_user.save()
      kakao_user = get_user_model().objects.get(username=kakao_id)
    
    return redirect("accounts:index")
    
    

