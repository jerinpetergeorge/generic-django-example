from django.db.models import SmallAutoField

from utils.db.functions import get_db_vendor


class TinyAutoField(SmallAutoField):
    def db_type(self, connection):
        vendor = get_db_vendor()
        if vendor == "mysql":
            return "tinyint AUTO_INCREMENT"
        return super().db_type(connection=connection)


def create_large_dataset(size=1000):
    from kn_dash.factory import PaymentTransactionFactory
    from kn_dash.models import PaymentTransaction
    for _ in range(size):
        PaymentTransaction.objects.bulk_create(
            PaymentTransactionFactory.build_batch(5000)
        )
        print(_)
