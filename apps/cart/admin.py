from django.contrib import admin
from .models import Voucher, Cart, CartItems

# Register your models here.

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):

    list_display = ['id_user', 'created', 'state', 'total_price']
    list_filter = ['created', 'total_price']
    ordering = ('created',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ['id_user', 'created', 'total']
    list_filter = ['created', 'id_user']
    exclude = ('total',)

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):

    list_display = ['id_cart', 'product', 'quantity', 'price']
    list_filter = ['id_cart',]
    exclude = ('price',)
