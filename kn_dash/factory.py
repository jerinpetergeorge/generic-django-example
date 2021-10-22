import random
from datetime import datetime

import factory
import pytz
from factory import fuzzy
from factory.django import DjangoModelFactory

from .models import PaymentTransaction


def calculate_total(model_instance: PaymentTransaction):
    return model_instance.fee + model_instance.amount


COUNTRY_CODES = [
    "MWK",
    "NZD",
    "BAM",
    "IRR",
    "SPL",
    "SDG",
    "NGN",
    "KRW",
    "SBD",
    "MKD",
    "USD",
]


class PaymentTransactionFactory(DjangoModelFactory):
    class Meta:
        model = PaymentTransaction

    transaction_id = factory.Faker("ssn")
    transaction_created = fuzzy.FuzzyDateTime(
        start_dt=datetime(2020, 1, 1, 0, 0, tzinfo=pytz.UTC)
    )
    type = fuzzy.FuzzyChoice(
        choice_tuple[0] for choice_tuple in PaymentTransaction.TYPE_CHOICES
    )
    gateway_code = factory.Faker(
        "pystr_format",
    )
    fee = factory.LazyAttribute(lambda _: random.randrange(10, 150))
    amount = factory.LazyAttribute(lambda _: random.randrange(10, 999999))
    total = factory.LazyAttribute(calculate_total)
    currency_code = fuzzy.FuzzyChoice(COUNTRY_CODES)
