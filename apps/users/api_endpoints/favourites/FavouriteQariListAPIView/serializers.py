from rest_framework import serializers

from apps.quran.models import Qari


class FavouriteQariListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qari
        fields = ("id", "full_name", "image", "juz_count")
