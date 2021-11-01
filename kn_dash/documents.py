from django.core.management import call_command
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import PaymentTransaction


@registry.register_document
class PaymentTransactionDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = "transactions"
        # See Elasticsearch Indices API reference for available settings
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = PaymentTransaction  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            "id",
            "transaction_id",
            "transaction_created",
            "state",
            "type",
            "gateway_code",
            "fee",
            "amount",
            "total",
            "currency_code",
            "state_changed_at",
        ]
