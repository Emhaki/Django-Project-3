from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):

  return render(request, "questions/index.html")

def create(request):
    form = QuestionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.user = request.user
        temp.save()
        return redirect("questions:index")
    context = {
        "form": form,
    }
    return render(request, "questions/create.html", context)

def myquestion(request):
  user = request.user
  questions = Question.objects.filter(user=user.pk)

  context = {
    "questions": questions,
  }

  return render(request, "questions/myquestion.html", context)