from django.db import models
from apps.users.models import User
from apps.products.models import Product
from uuid import uuid4

class Cart(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    total = models.PositiveIntegerField(default=0)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:

        db_table = 'carts'
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __str__(self) -> str:
        return str(self.id_user.username)

class CartItems(models.Model):

    id_cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    class Meta:

        db_table = 'cartsItems'
        verbose_name = 'cartItems'
        verbose_name_plural = 'cartsItems'

class Voucher(models.Model):

    code = models.UUIDField(default=uuid4, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveIntegerField()
    state = models.BooleanField(default=False)
    description_state = models.CharField(max_length=20, default="Preparacion")
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id_user.username)

    class Meta:

        db_table = 'voucher'
        verbose_name = 'vouchers'
        verbose_name_plural = 'vouchers'
