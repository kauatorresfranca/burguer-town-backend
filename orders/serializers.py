from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantidade', 'preco_unitario', 'total']

    def get_total(self, obj):
        return obj.total()

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'cliente', 'status', 'total', 'created_at', 'items']