from django.db.models import SmallAutoField

from utils.db.functions import get_db_vendor


class TinyAutoField(SmallAutoField):
    def db_type(self, connection):
        vendor = get_db_vendor()
        if vendor == "sqlite":
            return super().db_type(connection=connection)
        return "tinyint AUTO_INCREMENT"
