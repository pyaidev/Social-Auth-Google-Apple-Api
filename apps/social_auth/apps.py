from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SocialAuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.social_auth"
    verbose_name = _("Social Auth")

    def ready(self):
        from .post_social_login import register_signals

        register_signals()
