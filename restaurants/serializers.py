from rest_framework import serializers
from .models import RestaurantOwner, Restaurant
from UserAuth.serializers import ProfileSerializer, UserSerializer


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
            restaurant_owner = RestaurantOwner.objects.create(user=user, is_restaurant_owner=True,  is_employee=False)
            return restaurant_owner
        else:
            raise serializers.ValidationError(user_serializer.errors)


class RestaurantSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.user.username', read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'owner_name']

