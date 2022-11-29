from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("info/", views.info, name="info"),
    path("basket/", views.basket, name="basket"),
    path("payment/", views.payment, name="payment"),
    path("complete/", views.complete, name="complete"),
]
