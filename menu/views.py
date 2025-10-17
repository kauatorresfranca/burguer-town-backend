from rest_framework import viewsets
from .models import Section
from .serializers import SectionSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.prefetch_related('items').all()
    serializer_class = SectionSerializer