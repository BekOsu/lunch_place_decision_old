from django.urls import path
from .views import (
    RestaurantAPIView,
    RestaurantDetailView,
    MenuAPIView,
    MenuDetail,
    CurrentDayMenuView
)

urlpatterns = [
    path('ListCreate/', RestaurantAPIView.as_view(), name='restaurant_create'),
    path('detail/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('menus/', MenuAPIView.as_view(), name='menu_create'),
    path('menus/detail/<int:pk>/', MenuDetail.as_view(), name='menu_detail'),
    path('menus/current_day/', CurrentDayMenuView.as_view(), name='current_day_menu'),

]
