from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    # 주문 전 작품 상세 정보
    path("<int:art_pk>/info/", views.info, name="info"),
    # 장바구니
    path("mycart/", views.mycart, name="mycart"),
    path("mycart/<int:art_pk>/add/", views.add_cart, name="add_cart"),
    path("mycart/<int:cartitem_pk>/delete/", views.delete_cart, name="delete_cart"),
    # 주문
    path("create_order/", views.create_order, name="create_order"),
    path("order_delete/", views.order_delete, name="order_delete"),
    path("order_list/", views.order_list, name="order_list"),
    # 결제
    path("payment/", views.payment, name="payment"),
    path("complete/<int:user_pk>/", views.complete, name="complete"),
    # 결제 후 배송상태
    path("delivery/", views.delivery, name="delivery"),
    path("delivery_complete/", views.delivery_complete, name="delivery_complete"),
]
