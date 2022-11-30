from django.db import models
from config.settings import AUTH_USER_MODEL
from articles.models import Art

delivery_choices = (
    ("부재시 문 앞에 놓아주세요.", "부재시 문앞에 놓아주세요."),
    ("부재시 경비실에 맡겨주세요.", "부재시 경비실에 맡겨주세요."),
    ("부재시 전화 또는 문자주세요.", "부재시 전화 또는 문자 주세요."),
    ("택배함에 넣어주세요.", "택배함에 넣어주세요."),
    ("파손위험이 있는 상품입니다. 배송 시 주의해주세요.", "파손위험이 있는 상품입니다. 배송 시 주의해주세요."),
    ("배송 전에 연락주세요.", "배송 전에 연락주세요."),
)

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)    
    shipping_price = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=250, default="결제완료")
    contact_number = models.CharField(max_length=250, null=True)
    delivery_option = models.CharField(max_length=50, choices=delivery_choices)
    
class CartItem(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='user_cart', on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    # 장바구니에 담을 양
    quantity = models.PositiveIntegerField(default=0)
    # 장바구니 총 결제 금액
    def total(self):
        total = 0
        for art in self.art:
            total += art
        return total
    