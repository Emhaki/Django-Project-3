from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    # 주문 전 작품 상세 정보
    path("<int:art_pk>/info/", views.info, name="info"),
    # 장바구니
    path("mycart/", views.mycart, name="mycart"),
    path("mycart/<int:art_pk>/add/", views.add_cart, name="add_cart"),
    path("mycart/<int:art_pk>/delete/", views.delete_cart, name="delete_cart"),
    # 주문
    path("order_delete/", views.order_delete, name="order_delete"),
    path("order_list/", views.order_list, name="order_list"),
    # 결제
    path("payment/", views.payment, name="payment"),
    path("complete/", views.complete, name="complete"),
    # 결제 후 배송상태
    path("delivery/", views.delivery, name="delivery"),
    path("delivery_complete/", views.delivery_complete, name="delivery_complete"),
    # 약관 동의여부
    path("agree/", views.agree, name="agree"),
    # 가격 문의
    path("offer/", views.offer, name="offer"),
    path("offer/<int:art_pk>/create/", views.offer_create, name="offer_create"),
    path("offer_accept/<int:offer_pk>/", views.offer_accept, name="offer_accept")
]
