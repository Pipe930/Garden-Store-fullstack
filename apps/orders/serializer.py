from rest_framework import serializers
from .models import Order, Region, Province, Commune
from uuid import uuid4

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):

        order = Order.objects.create(**validated_data)

        return order

class RegionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Region
        fields = ["id", "name_region"]


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Province
        fields = ["id", "name_province"]

class CommuneSerializer(serializers.ModelSerializer):

    class Meta:

        model = Commune
        fields = ["id", "name_commune"]
