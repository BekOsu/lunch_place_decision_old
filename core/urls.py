from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RestaurantOwnerCreateView, EmployeeCreateView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('restaurant-owners/', RestaurantOwnerCreateView.as_view(), name='restaurant_owner_create'),
    path('employees/', EmployeeCreateView.as_view(), name='employee_create'),

]
