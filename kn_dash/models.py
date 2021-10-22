from django.db import models
from django.utils.translation import ugettext_lazy as _l
from django_extensions.db.models import TimeStampedModel


class PaymentTransaction(TimeStampedModel):
    """
    The core model of any payment transaction
    """

    CREATED = "created"
    PENDING = "pending"
    ATTEMPTED = "attempted"
    PAID = "paid"
    CANCELED = "canceled"
    EXPIRED = "expired"
    INVALID = "invalid"

    STATE_CHOICES = (
        # created in the API and returned to the merchant
        (CREATED, _l("Created")),
        # customer has opened the payment link and the request to the PSP was sent
        # (only available for payment requests created though
        (PENDING, _l("Pending")),
        # customer has attempted to pay, but failed due to various reasons
        (ATTEMPTED, _l("Attempted")),
        # ovio, no? :)
        (PAID, _l("Paid")),
        # only admin can mark as canceled
        (CANCELED, _l("Canceled")),
        # expired transactions which were not paid till a particular date
        (EXPIRED, _l("Expired")),
        # transactions which were invalidated due to various reasons.
        # IE: something changed in the knpay configuration and transaction
        # cannot be initialized anymore (missing currency, etc)
        (INVALID, _l("Invalid")),
    )

    E_COMMERCE = "e_commerce"
    PAYMENT_REQUEST = "payment_request"
    CUSTOMER_PAYMENT = "customer_payment"
    THIRD_PARTY = "third_party"
    TYPE_CHOICES = (
        # request from API, usually e-commerce
        (E_COMMERCE, _l("E-Commerce")),
        # Merchant requests for a payment to somebody
        (PAYMENT_REQUEST, _l("Payment request")),
        # customer pays by himself an amount to the merchant
        (CUSTOMER_PAYMENT, _l("Customer payment")),
        # Similar to e-commerce, but from third party providers
        # through plugins. IE: Shopify and Air Cairo
        (THIRD_PARTY, _l("Third party")),
    )

    transaction_id = models.CharField(_l("Transaction ID"), max_length=120)
    transaction_created = models.DateTimeField(_l("Created"))
    state = models.CharField(
        _l("state"), choices=STATE_CHOICES, default=PENDING, max_length=120
    )
    type = models.CharField(
        _l("Type"), choices=TYPE_CHOICES, default=E_COMMERCE, max_length=24
    )
    gateway_code = models.CharField(
        _l("Gateway code"), max_length=16, db_index=True, blank=True, default=""
    )
    fee = models.CharField(_l("Fee"), max_length=24, default="0")
    amount = models.CharField(_l("Amount"), max_length=24, default="0")
    total = models.CharField(_l("Total"), max_length=24, default="0")
    currency_code = models.CharField(_l("Currency code"), max_length=3)
    state_changed_at = models.DateTimeField(_l("State changed at"), null=True)

    def __unicode__(self):
        return "[{}] {} - {}".format(
            self.gateway_code or "gateway not selected",
            self.transaction_id,
            self.get_state_display(),
        )

    class Meta:
        verbose_name = _l("Payment transaction")
        verbose_name_plural = _l("Payment transactions")
        ordering = ("-created", "-modified")
