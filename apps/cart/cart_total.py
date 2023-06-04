from .models import Cart

# Method calculate cart total
def cart_total(id_cart):

    cart = Cart.objects.get(id=int(id_cart.id))

    items = cart.items.all()
    total = sum([item.quantity * item.product.price for item in items])

    cart.total = total
    cart.save()

# Method calculate total price
def calculate_total_price(items) -> int:

    total_price = 0

    for item in items:

        if item.product.id_offer is not None:

            discount = item.product.id_offer.discount
            price_product = item.product.price

            discount_decimal = discount / 100
            price_discount = price_product * discount_decimal

            price = price_product - price_discount

        else:

            price = item.product.price

        total_price += item.quantity * price

    return total_price

def calculate_total_quality(id_cart):

    cart = Cart.objects.get(id=id_cart)

    items = cart.items.all()

    total_quantity = 0

    for item in items:
        total_quantity += item.quantity

    cart.total_quantity = total_quantity
    cart.save()

    return total_quantity

def calculate_total_products(id_cart):

    cart = Cart.objects.get(id=id_cart)

    items = cart.items.all()

    quality_products = 0
    for item in items:
        quality_products += 1

    cart.total_products = quality_products
    cart.save()

    return quality_products
