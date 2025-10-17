from rest_framework import viewsets
from .models import Section, MenuItem
from .serializers import SectionSerializer, MenuItemSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.prefetch_related('items').all()
    serializer_class = SectionSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer