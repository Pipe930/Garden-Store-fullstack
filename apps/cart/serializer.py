from rest_framework import serializers
from .models import Cart, CartItems, Voucher
from apps.users.models import Subscription
from apps.products.models import Product
from django.http import Http404
from apps.products.discount import discount
from .cart_total import calculate_total_price, cart_total, calculate_total_quality, calculate_total_products
from .discount_stock import DiscountStock

class VoucherSerializer(serializers.ModelSerializer):

    class Meta:

        model = Voucher
        fields = "__all__"

    def create(self, validated_data):

        id_user = self.validated_data["id_user"]

        cart = obtain_cart_user(id_user)

        discount_stock = DiscountStock() # We instantiate the object DiscountStock

        discount_stock.discount_stock_product(cart.id)

        voucher = Voucher.objects.create(**validated_data)

        discount_stock.clean_cart(cart.id)

        cart_total(cart)

        return voucher

class CancelVoucherSerializer(serializers.ModelSerializer):

    id_user = serializers.CharField()
    state = serializers.BooleanField()

    class Meta:

        model = Voucher
        fields = ["state", "id_user"]

    def update(self, instance, validated_data):

        instance.state = validated_data.get('state', instance.state)

        instance.save()

        return instance

# Simple product serializer
class SimpleProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ["id", "name_product", "price"]

# Cart items serializer
class CartItemsSerializer(serializers.ModelSerializer):

    product = SimpleProductSerializer(many=False)
    price = serializers.SerializerMethodField(method_name="total")

    class Meta:

        model = CartItems
        fields = ["product", "quantity", "price"]

    # Method to calculate the total price
    def total(self, cartItem: CartItems):

        if cartItem.product.id_offer is not None:

            price = discount(cartItem.product.price, cartItem.product.id_offer.discount)

        else:
            price = cartItem.product.price

        result = cartItem.quantity * price

        cartItem.price = result
        cartItem.save()

        return result

# Cart serializer
class CartSerializer(serializers.ModelSerializer):

    items = CartItemsSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField(method_name="main_total")
    total_quantity = serializers.SerializerMethodField(method_name="calculate_total_quantity")
    total_products = serializers.SerializerMethodField(method_name="calculate_total_products")

    class Meta:

        model = Cart
        fields = ["id", "items", "total", "id_user", "total_quantity", "total_products"]

    def calculate_total_quantity(self, cart: Cart):

        total_quantity = calculate_total_quality(cart.id)

        return total_quantity

    def calculate_total_products(self, cart: Cart):

        quality_products = calculate_total_products(cart.id)

        return quality_products

    def main_total(self, cart: Cart):

        items = cart.items.all()
        total = calculate_total_price(items)

        if get_subscription(cart.id_user):

            discount_total = total * 0.05

            price_total_discount = total - discount_total

            cart.total = price_total_discount
            cart.save()

            return price_total_discount

        cart.total = total
        cart.save()

        return total

    def create(self, validated_data):

        cart = Cart.objects.create(**validated_data)
        return cart

def get_subscription(id_user):

    try:
        Subscription.objects.get(id_user = id_user)
    except Subscription.DoesNotExist:
        return False

    return True


# Add Cart serializer
class AddCartItemSerializer(serializers.ModelSerializer):

    id_user = serializers.IntegerField()

    class Meta:

        model = CartItems
        fields = ["product", "quantity", "id_user"]

    def save(self, **kwargs):

        product = self.validated_data["product"]
        quantity = self.validated_data["quantity"]
        id_user = self.validated_data["id_user"]

        cart = obtain_cart_user(id_user)

        if cart is None:
            raise serializers.ValidationError("Carrito no encontrado")

        id_cart = cart.id

        try:

            cartitem = CartItems.objects.get(product=product, id_cart=id_cart)

            if cartitem.product.stock > cartitem.quantity:

                cartitem.quantity += quantity
                cartitem.price = cartitem.quantity * cartitem.product.price

                cartitem.save()

                cart_total(cart)
                calculate_total_quality(cart.id)
                calculate_total_products(cart.id)

                self.instance = cartitem

        except CartItems.DoesNotExist:

            product2 = Product.objects.get(id=int(product.id))

            if product2.stock > quantity:

                newPrice = product2.price * quantity

                self.instance = CartItems.objects.create(
                    product=product,
                    id_cart=cart,
                    quantity=quantity,
                    price=newPrice
                    )

                cart_total(cart)
                calculate_total_products(cart.id)
                calculate_total_quality(cart.id)

        return self.instance

# Substract Cart serializer
class SubtractCartItemSerializer(serializers.ModelSerializer):

    id_user = serializers.IntegerField()

    class Meta:
        model = CartItems
        fields = ["product", "id_user"]

    def save(self, **kwargs):
        try:

            product = self.validated_data["product"]
            id_user = self.validated_data["id_user"]

            cart = obtain_cart_user(id_user)

            if cart is None:
                raise serializers.ValidationError("Carrito no encontrado")

            id_cart = cart.id

        except KeyError:
            raise Http404

        try:
            cartitem = CartItems.objects.get(product=product, id_cart=id_cart)
        except CartItems.DoesNotExist:
            raise serializers.ValidationError("Items no encontrado")

        if cartitem.quantity == 1:

            cartitem.delete()

            cart_total(cartitem.id_cart)
            calculate_total_products(cartitem.id_cart.id)
            calculate_total_quality(cartitem.id_cart.id)

            return self.instance

        cartitem.quantity -= 1
        cartitem.price = cartitem.quantity * cartitem.product.price
        cartitem.save()

        cart_total(cartitem.id_cart)
        calculate_total_products(cartitem.id_cart.id)
        calculate_total_quality(cartitem.id_cart.id)

        return self.instance

def obtain_cart_user(id_user:int):

    try:
        cart_user = Cart.objects.get(id_user=id_user)
    except Cart.DoesNotExist:
        return None

    return cart_user
