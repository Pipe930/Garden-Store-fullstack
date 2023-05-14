from rest_framework import serializers
from .models import Category, Product, Offer
from .discount import discount

# Serializer Offer Model
class SerializerOffer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ["id", "name_offer", "discount"]

# Serializer Product Model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    id_category = serializers.StringRelatedField()
    id_offer = SerializerOffer(many=False)
    price = serializers.SerializerMethodField(method_name="discount_price")

    def discount_price(self, product: Product):

        if product.id_offer is not None: # The product has a sale?

            # Function to make discount
            final_price = discount(product.price, product.id_offer.discount)

            return final_price

        return product.price

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
