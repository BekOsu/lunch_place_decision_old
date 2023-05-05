from rest_framework import serializers
from .models import RestaurantOwner, Employee, Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'user_email', 'user_first_name', 'is_restaurant_owner', 'is_employee']
        abstract = True


class RestaurantOwnerSerializer(ProfileSerializer):
    class Meta(ProfileSerializer.Meta):
        model = RestaurantOwner


class EmployeeSerializer(ProfileSerializer):
    class Meta(ProfileSerializer.Meta):
        model = Employee
