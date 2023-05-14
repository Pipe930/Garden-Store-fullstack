from rest_framework import serializers
from .models import Cart, CartItems, Voucher
from apps.products.models import Product
from django.http import Http404
from apps.products.discount import discount
from .cart_total import calculate_total_price, cart_total
from .discount_stock import DiscountStock

class VoucherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voucher
        fields = '__all__'

    def create(self, validated_data):

        id_cart = validated_data["id_cart"]

        discount_stock = DiscountStock()

        discount_stock.discount_stock_product(id_cart)

        voucher = Voucher.objects.create(**validated_data)

        discount_stock.clean_cart(id_cart)

        cart_total(id_cart)

        return voucher

class SimpleProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name_product', 'price', 'stock']

class CartItemsSerializer(serializers.ModelSerializer):

    product = SimpleProductSerializer(many=False)
    price = serializers.SerializerMethodField(method_name='total')

    class Meta:
        model = CartItems
        fields = ('id', 'id_cart', 'product', 'quantity', 'price')

    def total(self, cartItem: CartItems):
        if cartItem.product.id_offer is not None:

            price = discount(cartItem.product.price,  cartItem.product.id_offer.discount)

        price = cartItem.product.price

        result = cartItem.quantity * price
        return result

class CartSerializer(serializers.ModelSerializer):
    items = CartItemsSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField(method_name='main_total')
    class Meta:

        model = Cart
        fields = ('id', 'items', 'total', 'id_user')

    def main_total(self, cart: Cart):

        items = cart.items.all()
        total = calculate_total_price(items=items)
        return total

    def create(self, validated_data):
        cart = Cart.objects.create(**validated_data)
        return cart

class AddCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItems
        fields = ["product", "quantity", "id_cart"]

    def save(self, **kwargs):

        product = self.validated_data["product"]
        quantity = self.validated_data["quantity"]
        id_cart = self.validated_data["id_cart"]

        try:

            cartitem = CartItems.objects.get(product=product, id_cart=id_cart)
            if cartitem.product.stock > cartitem.quantity:

                cartitem.quantity += quantity
                cartitem.price = cartitem.quantity * cartitem.product.price

                cartitem.save()

                cart_total(id_cart)

                self.instance = cartitem

        except CartItems.DoesNotExist:

            product2 = Product.objects.get(id=int(product.id))

            newPrice = product2.price * quantity

            self.instance = CartItems.objects.create(
                product=product,
                id_cart=id_cart,
                quantity=quantity,
                price=newPrice
                )

            cart_total(id_cart)

        return self.instance

class SubtractCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItems
        fields = ["product", "id_cart"]

    def save(self, **kwargs):
        try:
            product = self.validated_data['product']
            id_cart = self.validated_data["id_cart"]

        except KeyError:
            raise Http404

        try:
            cartitem = CartItems.objects.get(product=product, id_cart=id_cart)
        except CartItems.DoesNotExist:
            raise Http404

        if cartitem.quantity == 1:
            cartitem.delete()

        cartitem.quantity -= 1
        cartitem.price = cartitem.quantity * cartitem.product.price
        cartitem.save()

        cart_total(cartitem.id_cart)

        return self.instance

class ClearCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItems
        fields = ("id_cart",)

    def save(self):
        try:
            id_cart = self.validated_data["id_cart"]
        except KeyError:
            raise Http404

        items = CartItems.objects.filter(id_cart=id_cart)

        for item in items:
            item.delete()

        return self.instance
