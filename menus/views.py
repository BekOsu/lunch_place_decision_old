from rest_framework.permissions import IsAuthenticated
from .models import Menu
from .serializers import MenuSerializer
from datetime import date
from rest_framework import generics, serializers
from UserAuth.permissions import IsRestaurantOwner
from UserAuth.permissions import IsEmployee


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
        queryset = Menu.objects.all()

        if self.request.user.is_authenticated:
            owner = self.request.user.restaurantowner
            queryset = queryset.filter(restaurant__owner=owner)
        else:
            queryset = queryset.none()

        return queryset


# class CurrentDayMenuView(generics.ListAPIView):
#     serializer_class = MenuSerializer
#     permission_classes = [IsAuthenticated, IsRestaurantOwner]
#
#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             owner = self.request.user.restaurantowner
#             today_menus = Menu.objects.filter(date=date.today(), restaurant__owner=owner)
#             return today_menus
#         else:
#             return Menu.objects.none()


class CurrentDayMenuView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if IsRestaurantOwner().has_permission(self.request, self):
                owner = self.request.user.restaurantowner
                today_menus = Menu.objects.filter(date=date.today(), restaurant__owner=owner)
                return today_menus
            elif IsEmployee().has_permission(self.request, self):
                today_menus = Menu.objects.filter(date=date.today())
                return today_menus
        return Menu.objects.none()
