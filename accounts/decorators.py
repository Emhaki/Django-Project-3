from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import User
from django.contrib import messages

from django.http import HttpResponse

def artist_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_creater:
            return function(request, *args, **kwargs)

        messages.info(request, "접근 권한이 없습니다.")
        return redirect("/")

    return wrap