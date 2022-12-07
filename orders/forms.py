from django import forms
from .models import CartItem, Order


class CartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = []
        labels = {}


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "username",
            "email",
            "address",
            "address_detail",
            "contact_number",
            "requests",
            "delivery_option",
        )
        labels = {
            "username": "이름",
            "email": "이메일",
            "address": "주소",
            "address_detail": "상세주소",
            "contact_number": "연락처",
            "requests": "기타 사항",
            "delivery_option": "요청 사항",
        }
        widgets = {
            "requests": forms.Textarea(
                attrs={
                    "placeholder": "요청사항을 적어주세요.",
                    "style": "width: 100%; height: 6rem; resize: none;",
                }
            ),
        }
