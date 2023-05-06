from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.user.username', read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'owner_name']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

