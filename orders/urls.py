from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("<int:art_pk>/info/", views.info, name="info"),
    path("basket/", views.basket, name="basket"),
    path("payment/", views.payment, name="payment"),
    path("complete/", views.complete, name="complete"),
    path("create_order/", views.create_order, name="create_order"),
    path("complete_order/", views.complete_order, name="complete_order"),
    path("order_delete/", views.order_delete, name="order_delete"),
    path("order_list/", views.order_list, name="order_list"),
    path("delivery/", views.delivery, name="delivery"),
    path("delivery_complete/", views.delivery_complete, name="delivery_complete"),
    path("mycart/", views.mycart, name="mycart"),
    path("add_cart/<int:art_pk>", views.add_cart, name="add_cart"),
]
