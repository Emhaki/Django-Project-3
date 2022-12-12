from django.shortcuts import render


def start(request):
    return render(request, "main/start.html")
