from django.contrib import admin
from .models import Voucher, Cart, CartItems

# Register your models here.

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):

    list_display = ['code', 'created', 'state', 'total_price', 'id_user', 'id_cart']
    list_filter = ['created', 'total_price']
    ordering = ('created',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ['created', 'total', 'id_user']
    list_filter = ['created', 'id_user']
    exclude = ('total',)

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):

    list_display = ['id_cart', 'product', 'quantity', 'price']
    list_filter = ['id_cart',]
    exclude = ('price',)
