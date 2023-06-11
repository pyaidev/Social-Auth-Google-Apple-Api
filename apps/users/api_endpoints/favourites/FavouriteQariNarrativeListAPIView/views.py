from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.quran.models import Qari

from .serializers import FavouriteQariNarrativeListSerializer


class FavouriteQariNarrativeView(ListAPIView):
    serializer_class = FavouriteQariNarrativeListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("full_name",)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Qari.objects.filter(favourite_qaris__user=self.request.user, narratives__audios__isnull=False)
