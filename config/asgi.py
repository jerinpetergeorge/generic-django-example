import os

from django.core.asgi import get_asgi_application

from .defaults import DEFAULT_DJANGO_SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS_MODULE)

application = get_asgi_application()
