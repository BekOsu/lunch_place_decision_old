from rest_framework import permissions
from core.models import RestaurantOwner, Employee


class IsRestaurantOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and RestaurantOwner.objects.filter(user=request.user).exists():
            return True
        return False


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return Employee.objects.filter(user=request.user).exists()
        return False
