from rest_framework import serializers
from ..models import Order, OrderItem
from .order_item_create import OrderItemCreateSerializer


class OrderCreateSerializer(serializers.ModelSerializer):
    itens = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ['cliente', 'status', 'itens']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')

        # Criar o pedido
        order = Order.objects.create(**validated_data)

        # Criar itens vinculados ao pedido
        for item in itens_data:
            OrderItem.objects.create(order=order, **item)

        return order
