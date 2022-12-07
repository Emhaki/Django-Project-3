from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.http import  JsonResponse

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
  questions = Question.objects.filter(user=request.user.pk)
  question = Question.objects.get(pk=request.user.pk)
  comments = question.comment_set.all().order_by('-pk')

  context = {
    "questions": questions,
    "comments": comments,
  }

  return render(request, "questions/myquestion.html", context)

def comment_create(request, question_pk):
    question_comment = get_object_or_404(Question, pk=question_pk)
    
    if request.user.is_authenticated:
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.question = question_comment
            comment.user = request.user
            comment.save()
            context = {
              'content': comment.content,
              'userName': comment.user.username,
              'created_at': comment.created_at
            }

        return JsonResponse(context)
    else:
        return redirect("accounts:login")