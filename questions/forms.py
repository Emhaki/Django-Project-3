from .models import *
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            "image",
            "title",
            "content",
        )
        labels = {
            "image": "이미지 첨부(선택)",
            "title": "문의 제목",
            "content": "문의 내용",
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content"
        ]