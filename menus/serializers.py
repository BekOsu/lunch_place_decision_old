from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.StringRelatedField(source='restaurant.name', read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'restaurant_name', 'date', 'items', 'created_at']
        read_only_fields = ['created_at']
