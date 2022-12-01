from django.shortcuts import render, redirect
from articles.models import Art
from .models import Order, CartItem
from .forms import CartForm
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone

User = get_user_model()


# Create your views here.
def basket(request):
    test = [1, 2, 3, 4, 5]
    context = {
        "content": test,
    }
    return render(request, "orders/basket.html", context)


def info(request, art_pk):
    art = Art.objects.get(pk=art_pk)
    cart_form = CartForm()
    context = {
        "art": art,
        "cart_form": cart_form,
        "content": "결제 정보 페이지",
    }
    return render(request, "orders/info.html", context)


def payment(request):
    context = {
        "content": "결제 페이지",
    }
    return render(request, "orders/payment.html", context)


def complete(request):
    context = {
        "content": "결제완료 페이지",
    }
    return render(request, "orders/complete.html", context)

def add_cart(request, art_pk):
    # 장바구니 담기
    art = Art.objects.get(pk=art_pk)
    
    if art.soldout == False:
        # cart = CartItem.objects.get(art_pk=art.pk, user_pk=request.user.pk)
        cart.quantity += 1
        cart.save()
        return redirect('orders:mycart')
    
    # 장바구니에 작품이 있다면 장바구니 가져오기
    try:
        cart = CartItem.objects.get(art__id=art.pk, user_id=request.user.pk)
    
    # 장바구니에 작품이 없다면 새롭게 저장
    except CartItem.DoesNotExist:
        user = User.objects.get(pk=request.user.pk)
        cart = CartItem(
            user = user,
            art = art,
            quantity = int(request.POST['quantity'])
        )
        cart.save()
    
    return redirect('orders:mycart')

def mycart(request):
    # 장바구니 가져오기
    cart_items = CartItem.objects.filter(user_id=request.user.pk)
    total_price = 0
    
    for each_total in cart_items:
        total_price += each_total.art.price
    
    if cart_items is not None:
        context = {
            'cart_items':cart_items,
            'total_price':total_price,
        }
        return render(request, 'orders/mycart.html', context)

# 장바구니 삭제

# 주문 생성
def create_order(request):
    shipping_name = request.user.username
    shipping_email = request.user.email
    # shipping_zipcode = request.user.zipcode
    # shipping_address = request.user.address
    
    # 장바구니 가져오기
    cart_items = CartItem.objects.filter(user_id=request.user.pk)
    
    # 장바구니 총 금액 
    total_price = 0
    for item in cart_items:
        total_price += item
    
    # 배송비
    if total_price >= 300000:
        delivery_fee = 0
    else:
         delivery_fee = 30000
    
    billing_amount = total_price + delivery_fee
    
    # 주문서
    if cart_items is not None:
        context = {
            "cart_items": cart_items,
            "total_price": total_price,
            # "shipping_address": shipping_address,
            "shipping_name": shipping_name,
            "shipping_email": shipping_email,
            "delivery_fee": delivery_fee,
            "billing_amount": billing_amount,
        }
        return render(request, "orders/order.html", context)
    else:
        return redirect("/")

# 주문 완료  
def complete_order(request):
    cart_items = CartItem.objects.filter(user_id=request.user.pk)
    shipping_address = request.GET.get("shipping_address")
    shipping_email = request.GET.get("shipping_email")

    for cart_item in cart_items:
        art = cart_item.art
                
        with transaction.atomic():
            order = Order(
                user=request.user,
                art=art,
                shipping_address=shipping_address,
                shipping_email=shipping_email,
            )
            order.save()
            
            art.soldout = True
            art.save()
            
    cart_items.delete()
    return render(request, "orders/complete_order.html")

# 주문 상세
# def detail(request):
#     return render(request, "orders/detail.html")

# 배송상태
def delivery(request, order_pk):
    order = Order.objects.get(pk=order_pk)
    order.created_at = timezone.now()
    order.order_status = "배송 준비중"
    order.save()
    return redirect("orders:order_list")

def delivery_complete(request, order_pk):
    order = Order.objects.get(pk=order_pk)
    order.created_at = timezone.now()
    order.order_status = "배송완료"
    order.save()
    return redirect("orders:order_list")

# 주문 취소
def order_delete(request, order_pk):
    # 주문 가져오기
    order = Order.objects.get(pk=order_pk)
    # 상품 가져오기
    art = Art.objects.get(pk=order.art.pk)
    # 주문 생성 시간을 취소시간으로 업데이트
    order.created_at = timezone.now()
    with transaction.atomic():
        # soldout 표시 제거
        art.soldout = False
        art.save()
        
        # 배송상태 변경
        order.order_status = "취소주문"
        order.save()
        
        return redirect("accounts:index", request.user.pk)

# 주문 내역 리스트
def order_list(request):
    # 결제 완료
    complete_orders = Order.objects.filter(order_status="결제완료").order_by("-created_at")
    # 취소한 주문
    cancel_orders = Order.objects.filter(order_status="취소주문").order_by("-created_at")
    # 배송 준비중
    delivery_orders = Order.objects.filter(order_status="배송 준비중").order_by("-created_at")
    # 배송 완료
    delivery_complete_orders = Order.objects.filter(order_status="배송완료").order_by("-created_at")
    
    context = {
        "complete_orders": complete_orders,
        "cancel_orders": cancel_orders,
        "delivery_orders": delivery_orders,
        "delivery_complete_orders": delivery_complete_orders,
    }
    return render(request, "orders/order_list.html", context)

