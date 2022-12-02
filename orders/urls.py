from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    # 주문 전 작품 상세 정보
    path("<int:art_pk>/info/", views.info, name="info"),
    path("basket/", views.basket, name="basket"),
    path("payment/", views.payment, name="payment"),
    path("complete/", views.complete, name="complete"),
    # 장바구니
    path("mycart/", views.mycart, name="mycart"),
    path("mycart/<int:art_pk>/add/", views.add_cart, name="add_cart"),
    # 주문
    path("create_order/", views.create_order, name="create_order"),
    path("complete_order/", views.complete_order, name="complete_order"),
    path("order_delete/", views.order_delete, name="order_delete"),
    path("order_list/", views.order_list, name="order_list"),
    path("delivery/", views.delivery, name="delivery"),
    path("delivery_complete/", views.delivery_complete, name="delivery_complete"),
]
