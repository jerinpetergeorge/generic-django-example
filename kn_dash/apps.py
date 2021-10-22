from django.apps import AppConfig


class KnDashConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "kn_dash"

    def ready(self):
        ...
