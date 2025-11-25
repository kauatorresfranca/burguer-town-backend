from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..serializers.order_create import OrderCreateSerializer
from ..serializers.order_read import OrderReadSerializer


@api_view(["POST"])
def order_create(request):
    serializer = OrderCreateSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        read_serializer = OrderReadSerializer(order)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)
    
    print(serializer.errors)  # <--- LOG MUITO IMPORTANTE
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
