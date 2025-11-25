from rest_framework import serializers
from menu.models import MenuItem
from orders.models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["menu_item", "quantidade", "preco_unitario"]
        read_only_fields = ["preco_unitario"]

    def create(self, validated_data):
        menu_item = validated_data["menu_item"]
        validated_data["preco_unitario"] = menu_item.price
        return super().create(validated_data)


