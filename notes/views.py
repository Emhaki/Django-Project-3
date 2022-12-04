from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .forms import *
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
# 보낸 DM과 받은 DM의 모달id값을 일치시키기 위해 pk값과 text값을 분리
dic = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

# @login_required
def index(request):
    notes = request.user.user_to.order_by("-created_at")  # 받은거
    to_notes = request.user.user_from.order_by("-created_at")  # 보낸거

    # 받은 편지 페이지네이션
    paginator = Paginator(notes, 10)
    page_number = request.GET.get("note")
    page_obj = paginator.get_page(page_number)

    # 보낸 편지 페이지네이션
    to_paginator = Paginator(to_notes, 10)
    to_page_number = request.GET.get("note")
    to_page_obj = to_paginator.get_page(to_page_number)

    context = {
        "notes": notes,
        "to_notes": to_notes,
        "page_obj": page_obj,
        "to_page_obj": to_page_obj,
    }

    return render(request, "notes/index.html", context)


# @login_required
def send(request, user_pk):
    notes = request.user.user_to.order_by("-created_at")
    to_user = get_object_or_404(get_user_model(), pk=user_pk)
    form = NotesForm(request.POST or None)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.from_user = request.user
        temp.to_user = to_user
        temp.save()

        text = ""
        for i in str(temp.pk):
            text += dic[i]
        temp.text = text
        temp.save()
        messages.success(request, "DM 전송 완료.😀")
        return redirect("notes:index")

    context = {
        "notes": notes,
        "to_user": to_user,
        "form": form,
    }
    return render(request, "notes/send.html", context)


# 버튼에 onclick을 걸어서 index에 보내고 index에서 데이터 받아올때 로직실행
# @login_required
def detail(request, note_pk):
    note = get_object_or_404(Notes, pk=note_pk)
    if request.user == note.to_user:
        if not note.read:
            note.read = True
            note.save()
        if not request.user.user_to.filter(read=False).exists():
            request.user.save()
        return render(request, "notes/detail.html", {"note": note})
    elif request.user == note.from_user:  # 보낸 사람일때는 내용은 보이고 읽음처리 x
        return render(request, "notes/detail.html", {"note": note})
    else:
        messages.error(request, "잘못된 접근입니다.😅")
        return redirect("notes:index")


# @login_required
def delete(request, note_pk):
    note = get_object_or_404(Notes, pk=note_pk)
    print(request.POST)
    if request.user == note.to_user and request.method == "POST":
        note.delete()
        return redirect("notes:index")
    else:
        messages.error(request, "남의 쪽지는 지울 수 없어요.😅")
        return redirect("notes:index")
