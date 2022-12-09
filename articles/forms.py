from django import forms
from .models import Art, Comment


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = (
            "art_category",
            "title",
            "art_size",
            "painted_year",
            "painted_way",
            "content",
            "image",
            "price",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
