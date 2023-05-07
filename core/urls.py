from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RestaurantOwnerList,
    RestaurantOwnerDetail,
    EmployeeList,
    EmployeeDetail,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('restaurant-owners/', RestaurantOwnerList.as_view(), name='restaurant_owner_List'),
    path('restaurant-owners/<int:pk>/', RestaurantOwnerDetail.as_view(), name='restaurant_owner_detail'),
    path('employees/', EmployeeList.as_view(), name='employee_List'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),

]
