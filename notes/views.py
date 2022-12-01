from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .forms import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
# @login_required
def index(request):
    notes = request.user.user_to.order_by("-created_at") # 받은거
    to_notes = request.user.user_from.order_by("-created_at") # 보낸거
    
    # 받은 편지 페이지네이션
    paginator = Paginator(notes, 10)
    page_number = request.GET.get("note")
    page_obj = paginator.get_page(page_number)

    # 보낸 편지 페이지네이션
    to_paginator = Paginator(to_notes, 10)
    to_page_number = request.GET.get("note")
    to_page_obj = to_paginator.get_page(to_page_number)

    context = {
        "notes":notes, 
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
        messages.success(request, "DM 전송 완료.😀")
        return redirect("notes:index")
    
    context = {
        "notes": notes,
        "to_user": to_user,
        "form": form,
    }
    return render(request, "notes/send.html", context)

# @login_required
def detail(request, note_pk):
    note = get_object_or_404(Notes, pk=note_pk)

    if request.user == note.to_user:
        if not note.read:
            note.read = True
            note.save()
        if not request.user.user_to.filter(read=False).exists():
            request.user.save()
        return render(request, "notes/detail.html", {"note":note})
    elif request.user == note.from_user:
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