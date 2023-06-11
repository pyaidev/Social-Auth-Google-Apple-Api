from allauth.account.adapter import get_adapter
from allauth.socialaccount.providers.apple.client import AppleOAuth2Client
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.views import LoginView as RestLoginView

from django.conf import settings

from . import serializers


class SocialLoginView(RestLoginView):
    serializer_class = serializers.SocialAuthLoginSerializer

    def process_login(self):
        get_adapter(self.request).login(self.request, self.user)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.OAUTH_CALLBACK_URL
    client_class = OAuth2Client


class AppleLogin(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
    callback_url = settings.OAUTH_CALLBACK_URL
    client_class = AppleOAuth2Client


__all__ = ["GoogleLogin", "AppleLogin"]
