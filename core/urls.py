from captcha import fields
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import include, path, re_path

from .schema import swagger_urlpatterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
    path("api/v1/social-auth/", include("apps.social_auth.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    re_path(r"^accounts/", include("allauth.urls"), name="socialaccount_signup"),
    path("api/v1/users/", include("apps.users.urls"), name="users"),
    re_path(r"^rosetta/", include("rosetta.urls")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
