from django.urls import path

from apps.social_auth import api_endpoints as views

app_name = "social-auth"

urlpatterns = [
    path("GoogleLogin", views.GoogleLogin.as_view(), name="GoogleLogin"),
    path("AppleLogin", views.AppleLogin.as_view(), name="AppleLogin"),
]
