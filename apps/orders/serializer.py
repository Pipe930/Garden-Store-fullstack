from rest_framework import serializers
from .models import Order, Region, Province, Commune, Branch
from uuid import uuid4

class OrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = "__all__"

    def validate(self, attrs):

        if attrs.get('id_branch') is None and attrs.get('id_commune') is None:
            raise serializers.ValidationError('Debe especificar al menos la sucursal o la comuna.')

        if attrs.get('id_branch') is not None and attrs.get('id_commune') is not None:
            raise serializers.ValidationError('Solo debe especificar uno, sucursal o la comuna.')

        if attrs.get('id_commune') and attrs.get('direction'):
            raise serializers.ValidationError('Si eligio envio a domicilio, tiene que indicar su direccion')

        return attrs

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

class BranchSerializer(serializers.ModelSerializer):

    class Meta:

        model = Branch
        fields = ["id", "name_branch"]
