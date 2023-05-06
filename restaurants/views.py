from rest_framework import generics
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer
from .permissions import IsRestaurantOwner, IsEmployee
from rest_framework.permissions import IsAuthenticated
from datetime import date


class RestaurantCreateView(generics.ListCreateAPIView):
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


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsRestaurantOwner]

    def perform_create(self, serializer):
        restaurant = self.request.user.restaurantowner.restaurant_set.first()
        serializer.save(restaurant=restaurant)


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsRestaurantOwner]


class CurrentDayMenuView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsEmployee]

    def get_queryset(self):
        today_menus = Menu.objects.filter(date=date.today())
        return today_menus
