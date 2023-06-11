from rest_framework import serializers

from apps.books.models import AudioBook


class FavouriteAudioBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ("id", "title", "image")
