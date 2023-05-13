from django.db import models
from apps.users.models import User
from apps.products.models import Product

class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    total = models.PositiveIntegerField(default=0)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:

        db_table = 'carts'
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __str__(self) -> str:
        return str(self.idUser.username)

class CartItems(models.Model):
    idCart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    class Meta:

        db_table = 'cartsItems'
        verbose_name = 'cartItems'
        verbose_name_plural = 'cartsItems'
