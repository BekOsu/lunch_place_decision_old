from django.urls import path
from .views import (
    MenuAPIView,
    MenuDetail,
    CurrentDayMenuView
)

urlpatterns = [
    path('', MenuAPIView.as_view(), name='menu_create'),
    path('detail/<int:pk>/', MenuDetail.as_view(), name='menu_detail'),
    path('current_day/', CurrentDayMenuView.as_view(), name='current_day_menu'),

]
