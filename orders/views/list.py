from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Order
from ..serializers.order_read import OrderReadSerializer


@api_view(["GET"])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderReadSerializer(orders, many=True)
    return Response(serializer.data)
