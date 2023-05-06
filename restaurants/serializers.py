from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.user.username', read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'owner_name']


class MenuSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.StringRelatedField(source='restaurant.name', read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'restaurant_name', 'date', 'items', 'created_at']
        read_only_fields = ['created_at']

