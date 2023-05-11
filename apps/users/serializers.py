from rest_framework import serializers
from .models import Subscription, User

# Serialized User Model
class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "is_active",
            "is_staff",
        )
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)
        return user

# Serialized Subscription Model
class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subscription
        fields = ("username", "email", "amount", "idUser")

    def create(self, validated_data):

        subscription = Subscription.objects.create(**validated_data)
        return subscription

# Send mail serializer
class MessageSerializer(serializers.Serializer):

    # Required attributes
    full_name = serializers.CharField(max_length=60)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=255)

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
