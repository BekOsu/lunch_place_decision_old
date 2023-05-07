from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['employee', 'menu', 'points', 'created_at']
        read_only_fields = ['created_at']

    def validate_points(self, value):
        if value < 1 or value > 3:
            raise serializers.ValidationError("Points must be between 1 and 3")
        return value
