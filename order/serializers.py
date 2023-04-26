from rest_framework import serializers

from customer.serializers import CustomerSerializer
from .models import Order


class OrderListSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    products = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['customer', 'description', 'count', 'total_amount', 'created_at', 'products']


class OrderSerializer(serializers.ModelSerializer):
    # customer = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    # products = serializers.SlugRelatedField(slug_field='name',many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['customer', 'description', 'count', 'total_amount', 'created_at', 'products']
