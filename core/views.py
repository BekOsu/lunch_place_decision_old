from rest_framework import generics
from .serializers import RestaurantOwnerSerializer, EmployeeSerializer
from .models import RestaurantOwner, Employee
from rest_framework.permissions import AllowAny


class RestaurantOwnerCreateView(generics.CreateAPIView):
    serializer_class = RestaurantOwnerSerializer
    queryset = RestaurantOwner.objects.all()
    permission_classes = [AllowAny]


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [AllowAny]
