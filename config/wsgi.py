import os

from django.core.wsgi import get_wsgi_application

from .defaults import DEFAULT_DJANGO_SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS_MODULE)

application = get_wsgi_application()
