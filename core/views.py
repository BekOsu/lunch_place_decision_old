from rest_framework import generics
from .serializers import RestaurantOwnerSerializer, EmployeeSerializer
from .models import RestaurantOwner, Employee
from rest_framework.permissions import AllowAny


class RestaurantOwnerList(generics.ListCreateAPIView):
    serializer_class = RestaurantOwnerSerializer
    queryset = RestaurantOwner.objects.all()
    permission_classes = [AllowAny]


class RestaurantOwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantOwner.objects.all()
    serializer_class = RestaurantOwnerSerializer


class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [AllowAny]


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
