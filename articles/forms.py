from django import forms
from .models import Art, Comment

class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['title', 'content', 'art_category', 'price', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]