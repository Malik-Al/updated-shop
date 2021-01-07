from rest_framework import serializers
from webapp.models import Product, Order, OrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'photo', 'price', 'in_order')


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'order', 'product', 'amount')


class OrderSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    order_products = OrderProductSerializer(many=True, read_only=True)     # вложенный serializers

    class Meta:
        model = Order
        fields = ('id', 'user', 'first_name', 'last_name', 'email',
                  'phone', 'status', 'created_at', 'updated_at', 'order_products')
