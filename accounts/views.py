from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
import requests
from django.contrib import messages
from random import random
from .forms import *
from articles.models import *
from orders.models import *
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
from django.contrib.auth.decorators import login_required
from accounts.decorators import artist_required

# Create your views here.


def index(request):
    return render(request, "accounts/index.html")


import secrets, os

state_token = secrets.token_urlsafe(16)
client_id = "064334979be24e5b57f6869948851f37"


def kakao_request(request):
    kakao_api = "https://kauth.kakao.com/oauth/authorize"
    redirect_uri = "http://nes-env.eba-9ycvw3yi.ap-northeast-2.elasticbeanstalk.com/accounts/kakao/login/callback"

    return redirect(
        f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    )


def kakao_callback(request):
    auth_code = request.GET.get("code")
    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": "http://nes-env.eba-9ycvw3yi.ap-northeast-2.elasticbeanstalk.com/accounts/kakao/login/callback",
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
        print(1111111111111111111111111111111111111111111111111)
        kakao_user = get_user_model().objects.get(test=kakao_id)
        # kakao_user.profileimage = kakao_profile_image
        kakao_user.refresh_token = refresh_token
        kakao_user.save()
        auth_login(
            request, kakao_user, backend="django.contrib.auth.backends.ModelBackend"
        )
        return redirect("articles:ticket_machine")
    else:
        kakao_login_user = get_user_model().objects.create(
            test=kakao_id,
            nickname=kakao_nickname,
            # profileimage=kakao_profile_image,
            email=kakao_email,
            refresh_token=refresh_token,
        )
        kakao_login_user.set_password(str(state_token))
        kakao_login_user.save()
        kakao_user = get_user_model().objects.get(test=kakao_id)
        auth_login(
            request, kakao_user, backend="django.contrib.auth.backends.ModelBackend"
        )
        return redirect("accounts:kakao_signup")


# 카카오 로그인
def kakao_signup(request):
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:ticket_machine")
    else:
        if request.GET:
            names = get_user_model().objects.filter(
                username=request.GET.get("username")
            )
            if names:
                context = {
                    "check": "True",
                }
                return JsonResponse(context)
            else:
                context = {
                    "check": "False",
                }
                return JsonResponse(context)
    return render(request, "accounts/kakao_signup.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.email = request.POST.get("email")
            forms.save()
            return redirect("accounts:login")
    else:
        if request.GET:
            names = get_user_model().objects.filter(
                username=request.GET.get("username")
            )
            if names:
                context = {
                    "check": "True",
                }
                return JsonResponse(context)
            else:
                context = {
                    "check": "False",
                }
                return JsonResponse(context)
    return render(request, "accounts/signup.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            context = {}
            return JsonResponse(context)
        else:
            user = get_user_model().objects.filter(username=request.POST["username"])
            if user.exists():
                context = {
                    "errorMsg": "잘못된 아이디 혹은 패스워드 입니다.",
                }
                return JsonResponse(context)
            else:
                context = {
                    "errorMsg": "존재하지 않는 회원입니다.",
                }
                return JsonResponse(context)
    else:
        return render(request, "accounts/login.html")


def logout(request):
    auth_logout(request)
    return redirect("accounts:login")


@login_required
# 소셜업데이트
def social(request):
    instagram = request.user.instagram
    github = request.user.github
    facebook = request.user.facebook

    if request.method == "POST":
        form = UpdateSocialForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect("accounts:profile", request.user.pk)

    context = {
        "instagram": instagram,
        "github": github,
        "facebook": facebook,
    }

    return render(request, "accounts/social_update.html", context)


# 프로필페이지
@login_required
def profile(request, user_pk):
    profiles = get_user_model().objects.filter(pk=user_pk)
    creater = get_user_model().objects.filter(pk=user_pk).filter(is_creater=1)
    # 작가가 등록한 작품들
    arts = Art.objects.filter(artist=user_pk).order_by()
    # paginator = Paginator(arts, 6)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    # 해당 유저가 좋아요를 누른 작품들
    art_likes = Art.objects.filter(likes=user_pk).order_by()
    # like_paginator = Paginator(art_likes, 6)
    # page_number = request.GET.get("like_page")
    # like_page_obj = like_paginator.get_page(page_number)

    # 해당 유저의 카트아이템
    user_carts = CartItem.objects.filter(user=user_pk)
    cart_paginator = Paginator(art_likes, 6)
    page_number = request.GET.get("cart_page")
    cart_page_obj = cart_paginator.get_page(page_number)

    # 구매내역 목록
    # art모델과 order모델에서 일치하는 작품명 필터링 + 결제완료 상태 필터링 + user_id=user_pk값인 것 필터링
    buys = Order.objects.filter(order_status="결제완료").filter(user_id=user_pk)
    list_ = []
    purchases = Art.objects.filter(order_id=999999999)
    if buys:
        for buy in buys:
            list_.append(str(buy.pk))
    purchases = Art.objects.filter(order_id__in=list_)
    # buy_paginator = Paginator(purchases, 6)
    # page_number = request.GET.get("buy_page")
    # buy_page_obj = buy_paginator.get_page(page_number)

    # 판매내역 목록
    soldouts = Art.objects.filter(soldout=True).filter(artist=user_pk)
    soldout_paginator = Paginator(soldouts, 6)
    page_number = request.GET.get("soldout_page")
    soldout_page_obj = soldout_paginator.get_page(page_number)

    context = {
        "profiles": profiles,
        "creater": creater,
        # 등록작품 관련
        "arts": arts,
        # "page_obj": page_obj,
        # 찜한 작품관련
        "art_likes": art_likes,
        # "like_page_obj": like_page_obj,
        # 구매관련
        "purchases": purchases,
        # "buy_page_obj": buy_page_obj,
        # 판매관련
        "soldouts": soldouts,
        "soldout_page_obj": soldout_page_obj,
        # 카트관련
        "user_carts": user_carts,
        "cart_page_obj": cart_page_obj,
    }
    return render(request, "accounts/profile.html", context)


# 프로필 업데이트
@login_required
def profile_update(request):
    creater_name = request.user.creater_name
    introduce = request.user.introduce
    email = request.user.email
    location = request.user.location
    location_detail = request.user.location_detail

    if request.method == "POST":
        form = UpdateDetailForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.save()
            return redirect("accounts:profile", request.user.pk)
    else:
        if request.GET:
            names = get_user_model().objects.filter(
                creater_name=request.GET.get("creater_name")
            )
            if names:
                context = {
                    "check": "True",
                }
                return JsonResponse(context)
            else:
                context = {
                    "check": "False",
                }
                return JsonResponse(context)
    context = {
        "creater_name": creater_name,
        "introduce": introduce,
        "email": email,
        "location": location,
        "location_detail": location_detail,
    }
    return render(request, "accounts/profile_update.html", context)


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
    if (valid_number and input_number != "") and valid_number == input_number:
        check = True
    else:
        check = False
    return JsonResponse({"check": check})


# 작가 인증
@login_required
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
    user_email2 = json.loads(request.body)["user_email2"]

    print(user_email)
    print(user_email2)
    if "ac.kr" in user_email[:] or "edu" in user_email[-4:]:
        email = EmailMessage(mail_subject, message, to=[user_email])
        email.send()
        check = True

    elif "ac.kr" in user_email2[:] or "edu" in user_email2[-4:]:
        email = EmailMessage(mail_subject, message, to=[user_email2])
        email.send()
        check = True
    else:
        check = False

    return JsonResponse({"validnumber": validnumber, "check": check})


def check_artist_number(request):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    valid_number = json.loads(request.body)["valid_number"]
    input_number = json.loads(request.body)["input_number"]
    print(user)
    if (valid_number and input_number != "") and valid_number == input_number:
        check = True
        user.is_creater = True
        user.save()
    else:
        check = False
    return JsonResponse(
        {
            "check": check,
        }
    )


@login_required
def recently(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    user_recently_view = user.recently_view
    user_recently_view = user_recently_view.replace("__", ",").replace("_", "")
    user_recently_view_list = user_recently_view.split(",")
    # print(user_recently_view_list)
    art_list = []
    try:
        while user_recently_view_list:
            target_pk = user_recently_view_list.pop()
            art = Art.objects.get(id=target_pk)
            art_list.append(art)
    except:
        pass
    context = {
        "art_list": art_list,
    }
    return render(request, "accounts/recently.html", context)


def find_id(request):
    users = get_user_model().objects.filter(email=request.GET["email"])
    if users.exists():
        user_list = []
        for user in users:
            if user.username == "":
                user_list.append(
                    "<span style='color: var(--highlight);'>Kakao acount</span>"
                )
            else:
                user_list.append(user.username)
        user_count = users.count()
        context = {
            "userList": user_list,
            "userCount": user_count,
        }
        return JsonResponse(context)
    else:
        context = {
            "errorMsg": "존재하지 않는 회원입니다.",
        }
        return JsonResponse(context)


def find_pw(request):
    if get_user_model().objects.filter(username=request.GET["username"]).exists():
        user = get_user_model().objects.get(username=request.GET["username"])
        context = {
            "userEmail": user.email,
            "userName": user.username,
        }
        return JsonResponse(context)
    else:
        context = {
            "errorMsg": "존재하지 않는 회원입니다.",
        }
        return JsonResponse(context)


# 비밀번호 찾기 이메일 인증
def find_pw_email(request):
    validnumber = round(random() * 10000)
    current_site = get_current_site(request)
    message = render_to_string(
        "accounts/reset_pw.html",
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
    user_email = request.POST["user_email"]
    user_name = request.POST["user_name"]
    email = EmailMessage(mail_subject, message, to=[user_email])
    email.send()

    context = {
        "userName": user_name,
        "validnumber": validnumber,
    }
    return JsonResponse(context)


def find_pw_email_check(request):
    input_number = request.POST["inputNum"]
    valid_number = request.POST["validNum"]
    if (valid_number and input_number != "") and valid_number == input_number:
        user = get_user_model().objects.get(username=request.POST["userName"])
        check = True
        context = {
            "userName": user.username,
            "check": check,
        }
    else:
        check = False
        context = {
            "check": check,
        }
    return JsonResponse(context)


def pw_change(request):
    user = get_user_model().objects.get(username=request.POST["userName"])
    if request.method == "POST":
        if request.POST["pw1"] == request.POST["pw2"] and len(request.POST["pw1"]) >= 8:
            user.set_password(request.POST["pw1"])
            user.save()
            context = {
                "msg": "변경에 성공하였습니다.",
            }
            return JsonResponse(context)
        else:
            context = {
                "msg": "변경에 실패하였습니다.",
            }
            return JsonResponse(context)
