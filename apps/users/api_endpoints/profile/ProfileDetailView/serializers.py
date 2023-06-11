from rest_framework import serializers

from apps.users.models import User


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "avatar")
