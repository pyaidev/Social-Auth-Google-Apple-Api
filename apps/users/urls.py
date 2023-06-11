from rest_framework.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .api_endpoints import (
    ProfileDetailView,
    ProfileUpdateView,
    TokenGenerationView,
)

app_name = "users"


urlpatterns = [
    path("ProfileDetail", ProfileDetailView.as_view(), name="ProfileDetail"),
    path("ProfileUpdate", ProfileUpdateView.as_view(), name="ProfileUpdate"),
    path("Token", TokenGenerationView.as_view(), name="Token"),
    path("TokenRefresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("TokenVerify", TokenVerifyView.as_view(), name="token_verify"),
]
