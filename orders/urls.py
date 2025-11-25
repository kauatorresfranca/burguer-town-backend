from django.urls import path
from .views.create import order_create
from .views.list import order_list
urlpatterns = [
    path('create/', order_create, name='create_order'),
    path('', order_list, name='list_orders'),
]
