from django.db import models
from config.settings import AUTH_USER_MODEL
from articles.models import Art

delivery_choices = (
    ("부재시 문 앞에 놓아주세요.", "부재시 문 앞에 놓아주세요."),
    ("부재시 경비실에 맡겨주세요.", "부재시 경비실에 맡겨주세요."),
    ("부재시 전화 또는 문자주세요.", "부재시 전화 또는 문자 주세요."),
    ("택배함에 넣어주세요.", "택배함에 넣어주세요."),
    ("파손위험이 있는 상품입니다. 배송 시 주의해주세요.", "파손위험이 있는 상품입니다. 배송 시 주의해주세요."),
    ("배송 전에 연락주세요.", "배송 전에 연락주세요."),
)

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "장바구니"
        verbose_name_plural = f"{verbose_name} 목록"
        ordering = ["-pk"]

    # 장바구니 총 결제 금액
    def total(self):
        total = 0
        for art in self.art:
            total += art
        return total


# 게시글(art) - 댓글(order)
# order(댓글) 1 : art(게시글) 1
# 게시글 1 : 댓글 N


# 유저 1 : 주문 N
# 그림 1 : 주문 N -> 주문 1 : 그림 N
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=250, default="결제완료")  

    # 사용자 주문 정보
    username = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    address_detail = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=250)
    requests = models.TextField(max_length=100, null=True, blank=True)
    delivery_option = models.CharField(
        max_length=50, choices=delivery_choices, default="부재시 문 앞에 놓아주세요."
    )
    

