from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

# Create your views here.
def main(request):
    return render(request, "main/main.html")
