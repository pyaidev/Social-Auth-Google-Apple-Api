from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.profile.ProfileDetailView.serializers import (
    ProfileDetailSerializer,
)


class ProfileDetailView(RetrieveAPIView):
    serializer_class = ProfileDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
