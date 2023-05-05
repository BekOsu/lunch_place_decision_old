from django.urls import path
from .views import (
    RestaurantCreateView,
    RestaurantUpdateView,
    MenuCreateView,
    MenuDetail,
    CurrentDayMenuView
)

urlpatterns = [
    path('restaurants/create/', RestaurantCreateView.as_view(), name='restaurant_create'),
    path('restaurants/update/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('menus/create/', MenuCreateView.as_view(), name='menu_create'),
    path('menus/list/', MenuDetail.as_view(), name='menu_list'),
    path('menus/update/<int:pk>/', MenuDetail.as_view(), name='menu_update'),
    path('menus/current_day/', CurrentDayMenuView.as_view(), name='current_day_menu'),

]
