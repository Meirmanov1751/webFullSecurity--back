from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'executor', 'name', 'description', 'price', 'is_available']


class ProductListSerializer(serializers.ModelSerializer):
    executor = serializers.SlugRelatedField(slug_field='first_name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'executor', 'name', 'description', 'price', 'is_available']
