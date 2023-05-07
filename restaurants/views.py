from rest_framework import generics
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer
from .permissions import IsRestaurantOwner
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from datetime import date


class RestaurantAPIView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, IsRestaurantOwner]

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user.restaurantowner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.restaurantowner)


class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, IsRestaurantOwner]
    queryset = Restaurant.objects.all()

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user.restaurantowner)


class MenuAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsRestaurantOwner]

    def get_queryset(self):
        owner = self.request.user.restaurantowner
        return Menu.objects.filter(restaurant__owner=owner)

    def perform_create(self, serializer):
        owner = self.request.user.restaurantowner
        restaurant = owner.restaurant_set.first()

        if restaurant:
            serializer.save(restaurant=restaurant)
        else:
            raise serializers.ValidationError("You must own a restaurant to create a menu.")


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsRestaurantOwner]

    def get_queryset(self):
        owner = self.request.user.restaurantowner
        return Menu.objects.filter(restaurant__owner=owner)


class CurrentDayMenuView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        today_menus = Menu.objects.filter(date=date.today())
        return today_menus
