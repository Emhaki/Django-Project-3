from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            "username",
            "email",
            "nickname",
            "location",
        )
        labels = {
            "username": "아이디",
            "email": "이메일",
            "nickname": "이름",
            "location": "주소"
        }