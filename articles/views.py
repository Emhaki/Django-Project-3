from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


def main(request):
    return render(request, "articles/main.html")
