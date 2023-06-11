from rest_framework import serializers

from apps.books.models import Book


class FavouriteBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "image")
