from rest_framework import serializers
from ..models import Order
from .order_item_read import OrderItemSerializer

class OrderReadSerializer(serializers.ModelSerializer):
    itens = OrderItemSerializer(many=True, read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'cliente', 'status', 'created_at', 'total', 'itens']
        read_only_fields = ['created_at']
