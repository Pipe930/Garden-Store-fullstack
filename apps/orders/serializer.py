from rest_framework import serializers
from .models import Order
from uuid import uuid4

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):

        order = Order.objects.create(**validated_data)

        return order
