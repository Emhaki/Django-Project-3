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
    # carts = models.ManyToManyField(Art, related_name = 'carts_user')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    # active = models.BooleanField(default=False)
    # 장바구니에 담을 양
    # quantity = models.PositiveIntegerField(default=0)
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

    # def __init__(self, price):
    #     self.art.price = price

    # def __str__(self):
    #     return (self.art)


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=250, default="결제완료")
    

    # 사용자 주문 정보
    username = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    address_detail = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=250, null=True)
    requests = models.TextField(max_length=100, null=True)
    delivery_option = models.CharField(
        max_length=50, choices=delivery_choices, default="부재시 문 앞에 놓아주세요."
    )
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order {self.id}"

    def get_total_product(self):
        return sum(item.get_item_price() for item in self.art.price.all())

    def get_total_price(self):
        total_product = self.get_total_product()
        if total_product >= 30000:
            total_product += 3000
        else:
            total_product += 0
        return total_product
