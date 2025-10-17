from rest_framework import serializers
from .models import Section, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'description', 'price', 'image', 'section']

class SectionSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'name', 'items']