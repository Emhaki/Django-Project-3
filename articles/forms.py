from django import forms
from .models import Art, Comment


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ("art_category",)

        labels = {
            "art_category": "카테고리",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
