from apps.products.models import Product
from .models import CartItems

class DiscountStock():

    def get_object(self, id_product:int):

        try:
            product = Product.objects.get(id=id_product)
        except Product.DoesNotExist:
            return 0

        return product

    def discount_stock_product(self, id_cart:int):

        cartitems_user = CartItems.objects.filter(id_cart=id_cart)

        for items in cartitems_user:

            quantity_item = items.quantity
            product_stock = items.product.stock

            new_stock = product_stock - quantity_item

            product = self.get_object(items.product.id)

            product.stock = new_stock

            product.save()

    def clean_cart(self, id_cart:int):

        cartitems_user = CartItems.objects.filter(id_cart=id_cart)

        for items in cartitems_user:
            items.delete()
