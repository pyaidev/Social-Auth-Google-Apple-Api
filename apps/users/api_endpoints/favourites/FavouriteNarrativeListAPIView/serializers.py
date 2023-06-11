from rest_framework import serializers

from apps.books.models import Narratives


class FavouriteNarrativeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Narratives
        fields = ("id", "title", "image")
