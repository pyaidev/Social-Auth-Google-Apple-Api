from rest_framework import serializers

from apps.users.models import FavouriteZikr
from apps.zikr.models import Zikr


class FavouriteZikrListSerializer(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = Zikr
        fields = (
            "id",
            "title",
            "category",
            "arabic",
            "transliteration",
            "translation",
            "audio",
            "order",
            "created_at",
            "updated_at",
            "is_favourite",
        )

    def get_is_favourite(self, obj):
        if self.context.get("request").user.is_authenticated:
            return FavouriteZikr.objects.filter(user=self.context.get("request").user, zikr=obj).exists()
        return False
