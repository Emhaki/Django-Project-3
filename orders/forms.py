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
        fields = ['email', 'address', 'zip_code', 'city']
