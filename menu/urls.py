from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SectionViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r'sections', SectionViewSet)
router.register(r'menuitems', MenuItemViewSet)  # Adiciona o endpoint /api/menuitems/

urlpatterns = [
    path('', include(router.urls)),
]