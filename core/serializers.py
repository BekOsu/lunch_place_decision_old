from rest_framework import serializers
from .models import RestaurantOwner, Employee, Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'user_email', 'user_first_name', 'is_restaurant_owner', 'is_employee']
        abstract = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
        )
        return user


class RestaurantOwnerSerializer(ProfileSerializer):
    user = UserSerializer()

    class Meta(ProfileSerializer.Meta):
        model = RestaurantOwner
        fields = ProfileSerializer.Meta.fields + ['user', 'is_restaurant_owner']
        read_only_fields = ['id', 'is_restaurant_owner']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            restaurant_owner = RestaurantOwner.objects.create(user=user, is_restaurant_owner=True)
            return restaurant_owner
        else:
            raise serializers.ValidationError(user_serializer.errors)


class EmployeeSerializer(ProfileSerializer):
    user = UserSerializer()

    class Meta(ProfileSerializer.Meta):
        model = Employee
        fields = ProfileSerializer.Meta.fields + ['user', 'is_employee']
        read_only_fields = ['id', 'is_employee']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            employee = Employee.objects.create(user=user, is_employee=True)
            return employee
        else:
            raise serializers.ValidationError(user_serializer.errors)
