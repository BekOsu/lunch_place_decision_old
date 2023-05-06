from django.urls import path
from .views import (
    RestaurantCreateView,
    RestaurantDetailView,
    MenuCreateView,
    MenuDetail,
    CurrentDayMenuView
)

urlpatterns = [
    path('ListCreate/', RestaurantCreateView.as_view(), name='restaurant_create'),
    path('detail/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('menus/create/', MenuCreateView.as_view(), name='menu_create'),
    # path('menus/list/', MenuDetail.as_view(), name='menu_list'),
    # path('menus/update/<int:pk>/', MenuDetail.as_view(), name='menu_update'),
    # path('menus/current_day/', CurrentDayMenuView.as_view(), name='current_day_menu'),

]
