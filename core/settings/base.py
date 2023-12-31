"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import sys
from datetime import timedelta
from pathlib import Path

import environ

from core.jazzmin_conf import *  # noqa

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# READING ENV
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = ["*"]

# Application definition
DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = ["apps.common", "apps.users", "apps.social_auth"]

THIRD_PARTY_APPS = [
    "drf_yasg",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "social_django",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.apple",
    "ckeditor",
    "ckeditor_uploader",
    "modeltranslation",
    "django_filters",
    "rosetta",
    "auditlog",
    "captcha",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/second", "user": "100/second"},
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "EXCEPTION_HANDLER": "apps.common.exception_handler.custom_exception_handler",
}

# JWT settings

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=20),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}

TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

if TESTING:
    del REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "auditlog.middleware.AuditlogMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

AUTH_USER_MODEL = "users.User"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env.str("DB_ENGINE"),
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.get_value("DB_PASSWORD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = (BASE_DIR / "staticfiles",)

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CACHES
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"{env.str('REDIS_URL', 'redis://localhost:6379/0')}",
        "KEY_PREFIX": "boilerplate",  # todo: you must change this with your project name or something else
    }
}

# CELERY CONFIGURATION
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", "redis://localhost:6379")
CELERY_RESULT_BACKEND = env.str("CELERY_BROKER_URL", "redis://localhost:6379")

CELERY_TIMEZONE = "Asia/Tashkent"

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 300 * 60

CKEDITOR_UPLOAD_PATH = "ckeditor"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_CONFIGS = {
    "default": {
        # 'skin': 'moono',
        "width": "100%",
        "skin": "office2013",
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_YourCustomToolbarConfig": [
            {"name": "document", "items": ["Source", "-", "Save", "NewPage", "Preview", "Print", "-", "Templates"]},
            {"name": "clipboard", "items": ["Cut", "Copy", "Paste", "PasteText", "PasteFromWord", "-", "Undo", "Redo"]},
            {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
            {
                "name": "forms",
                "items": [
                    "Form",
                    "Checkbox",
                    "Radio",
                    "TextField",
                    "Textarea",
                    "Select",
                    "Button",
                    "ImageButton",
                    "HiddenField",
                ],
            },
            "/",
            {
                "name": "basicstyles",
                "items": ["Bold", "Italic", "Underline", "Strike", "Subscript", "Superscript", "-", "RemoveFormat"],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "CreateDiv",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "BidiLtr",
                    "BidiRtl",
                    "Language",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            {
                "name": "insert",
                "items": [
                    "Image",
                    "Flash",
                    "Table",
                    "Upload",
                    "HorizontalRule",
                    "Smiley",
                    "SpecialChar",
                    "PageBreak",
                    "Iframe",
                ],
            },
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
            {"name": "about", "items": ["About"]},
            "/",  # put this to force next toolbar on new line
            {
                "name": "yourcustomtools",
                "items": [
                    # put the name of your editor.ui.addButton here
                    "Preview",
                    "Maximize",
                    "base64image",
                    "Youtube",
                ],
            },
            {
                "name": "texttransform",
                "items": [
                    "TransformTextToUppercase",
                    "TransformTextToLowercase",
                    "TransformTextCapitalize",
                    "TransformTextSwitcher",
                ],
            },
        ],
        "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "uploadimage",  # the upload image feature
                # your extra plugins here
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                # 'devtools',
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
                "base64image",
                "texttransform",
                "youtube",
            ]
        ),
    }
}

# SOCIAL AUTH CONFIGURATION
SOCIALACCOUNT_PROVIDERS = {  # noqa
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
    "apple": {
        "APP": {
            # Your service identifier.
            "client_id": env.str("SOCIALACCOUNT_APPLE_CLIENT_ID", "https://github.com/nurmukhammaddev"),
            # The Key ID (visible in the "View Key Details" page).
            "secret": env.str("SOCIALACCOUNT_APPLE_SECRET", "6DP9RD92NY"),
            # Member ID/App ID Prefix -- you can find it below your name
            # at the top right corner of the page, or it’s your App ID
            # Prefix in your App ID.
            "key": env.str("SOCIALACCOUNT_APPLE_TEAM_ID", "KHGXWF53U9"),  # team id
            # The certificate you downloaded when generating the key.
            "certificate_key": """-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgL3oIve1fiKQJx0gl
SLQkQG8zyhwhMbg/TSajVdVuURigCgYIKoZIzj0DAQehRANCAASplpoy6+148IwB
CZahdME/LeHIziIHGTNIZQOAIRYdNQNugfiYZI9RnV/07wK0bYb8hWB65TXz5Kek
szdGoZ+F
-----END PRIVATE KEY-----""",
        }
    },
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env.str("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", "")  # noqa
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env.str("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", "")  # noqa

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

OAUTH_CALLBACK_URL = f"{env.str('HOST', '')}/login"

GOOGLE_CLIENT_ID = env.str("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = env.str("GOOGLE_CLIENT_SECRET", "")

REST_USE_JWT = True

gettext = lambda s: s  # noqa: E731
LANGUAGES = (
    ("uz", gettext("Uzbek")),
    ("uk", gettext("Uzbek Cyrillic")),
    ("en", gettext("English")),
    ("ru", gettext("Russian")),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"

MODELTRANSLATION_LANGUAGES_CHOICES = (
    ("uz", gettext("Uzbek")),
    ("uk", gettext("Uzbek Cyrillic")),
    ("en", gettext("English")),
    ("ru", gettext("Russian")),
)


# DJANGO RESIZED IMAGE FIELDS
DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 85
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = "WEBP"
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {"WEBP": ".webp"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

OPTIMIZED_IMAGE_METHOD = "pillow"

AUDITLOG_INCLUDE_ALL_MODELS = True

RECAPTCHA_PUBLIC_KEY = env.str("RECAPTCHA_PUBLIC_KEY", "MyRecaptchaPublicKey123")
RECAPTCHA_PRIVATE_KEY = env.str("RECAPTCHA_PRIVATE_KEY", "MyRecaptchaPrivateKey123")

MAX_QUERY_COUNT = 30000

DATA_UPLOAD_MAX_NUMBER_FIELDS = 30000

DATA_UPLOAD_MAX_MEMORY_SIZE = 367001600  # 350 MB
