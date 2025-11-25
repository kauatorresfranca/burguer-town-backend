from rest_framework import serializers
from orders.models import OrderItem

class OrderItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ["menu_item", "quantidade", "preco_unitario"]
        read_only_fields = ["preco_unitario"]

    def validate(self, data):
        menu_item = data["menu_item"]
        data["preco_unitario"] = menu_item.price
        return data