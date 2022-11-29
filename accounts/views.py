from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

# Create your views here.

def index(request):
  return render(request, "accounts/index.html")

def signup(request):

  return render(request, "accounts/signup.html")

def login(request):

  return render(request, "accounts/login.html")