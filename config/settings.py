from datetime import timedelta
from pathlib import Path

import sentry_sdk
from environ import Env
from sentry_sdk.integrations.django import DjangoIntegration

env = Env()

# option to attach an env file
# default location is `.env-dir/local`
# if file not found, simply ignored
env.read_env(env("ENV_FILE", default=".envs/.env"))

# GENERAL
# ------------------------------------------------------------------------------
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = "j2@-mwo#(8k%l9f%zugc=^1%ug9-&xh4wmj!g@6uop@^l%run_"
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env("DEBUG", bool, default=False)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
EXTRA_ALLOWED_HOSTS = env("EXTRA_ALLOWED_HOSTS", list, default=[])
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", *EXTRA_ALLOWED_HOSTS]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# APPS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
LOCAL_APPS = [
    # Local
    "accounts",
    "pages",
    "polls",
    "extra",
    "attendance",
]
THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "crispy_forms",
    "debug_toolbar",
    "drf_yasg",
    "django_extensions",
    "rest_framework",
    "drf_spectacular",
    "rest_framework_simplejwt",
    "django_su",
]
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party
    *THIRD_PARTY_APPS,
    # local apps
    *LOCAL_APPS,
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db()}

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
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

# INTERNATIONALIZATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/topics/i18n/
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-USE_I18N
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]
# http://whitenoise.evans.io/en/stable/django.html#add-compression-and-caching-support
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# DJANGO-CRISPY-FORMS CONFIGS
# ------------------------------------------------------------------------------
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap4"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_CONFIG = env.email_url(default="smtp://user:password@localhost:25")
vars().update(EMAIL_CONFIG)

# DJANGO-DEBUG-TOOLBAR CONFIGS
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips
INTERNAL_IPS = ["127.0.0.1"]

# CUSTOM USER MODEL CONFIGS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "accounts.User"

CACHES = {
    "default": {
        "BACKEND": "core.redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL", default="redis://localhost:6379"),
    },
}

# DJANGO-ALLAUTH CONFIGS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "home"
# https://django-allauth.readthedocs.io/en/latest/views.html#logout-account-logout
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
# https://django-allauth.readthedocs.io/en/latest/installation.html?highlight=backends
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_ADAPTER = "core.allauth.adapter.SocialAccountAdapter"

# Development Environment Items
DJANGO_SU_CONFIG = {
    "USERNAME_FIELD": "email",
    "USERNAME": env("DJANGO_SU_USERNAME", default="admin@admin.com"),
    "PASSWORD": env("DJANGO_SU_PASSWORD", default="password"),
    "EXTRA_ARGS": {
        "full_name": env("DJANGO_SU_FULL_NAME", default="Admin"),
    },
}

REST_FRAMEWORK = {
    # YOUR SETTINGS
    "DEFAULT_SCHEMA_CLASS": "core.drf_spectacular.schema.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",  # default
        "rest_framework.authentication.BasicAuthentication",  # default
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "DRF Spectacular API",
    "DESCRIPTION": "Your project description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "POSTPROCESSING_HOOKS": [
        "core.drf_spectacular.hooks.post_hook__add_global_header",
    ],
    "PREPROCESSING_HOOKS": [
        "core.drf_spectacular.hooks.pre_hook__add_global_header",
    ],
}

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=5),
}

# Celery Config
# https://docs.celeryq.dev/en/stable/userguide/configuration.html
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://localhost:6379/5")


#
SENTRY_DSN = env("SENTRY_DSN", default="")
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[
        DjangoIntegration(
            transaction_style="url",
            middleware_spans=True,
            signals_spans=False,
            cache_spans=False,
        ),
    ],
)
