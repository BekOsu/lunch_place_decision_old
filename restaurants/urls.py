from django.urls import path
from .views import (
    RestaurantOwnerList,
    RestaurantOwnerDetail,
    RestaurantAPIView,
    RestaurantDetailView,
    MenuAPIView,
    MenuDetail,
    CurrentDayMenuView
)

urlpatterns = [
    # restaurant-owners/
    path('restaurant-owners/', RestaurantOwnerList.as_view(), name='restaurant_owner_List'),
    path('restaurant-owners/<int:pk>/', RestaurantOwnerDetail.as_view(), name='restaurant_owner_detail'),
    # Restaurant
    path('ListCreate/', RestaurantAPIView.as_view(), name='restaurant_create'),
    path('detail/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    # menus
    path('menus/', MenuAPIView.as_view(), name='menu_create'),
    path('menus/detail/<int:pk>/', MenuDetail.as_view(), name='menu_detail'),
    path('menus/current_day/', CurrentDayMenuView.as_view(), name='current_day_menu'),

]
