from rest_framework import serializers
from .models import Category, Product, Offer

class SerializerOffer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'name_offer', 'discount']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    id_category = serializers.StringRelatedField()
    id_offer = SerializerOffer(many=False)
    price = serializers.SerializerMethodField(method_name='discount')

    def discount(self, product: Product):

        if product.id_offer is not None:

            discount = product.id_offer.discount
            priceProduct = product.price

            discountDecimal = discount / 100
            priceDiscount = priceProduct * discountDecimal

            result = priceProduct - priceDiscount

            return result

        return product.price

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
