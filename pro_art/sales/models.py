import datetime

from django.db import models
from django.db import transaction

from share.models import TimeStampedModel
from users.models import UserProfile
from products.models import Product

STATUS_ORDER = (
    ('CANCELED', 'CANCELED'),
    ('PENDING', 'PENDING'),
    ('PAID', 'PAID'),
    ('INVOICED', 'INVOICED'),
)


class Order(TimeStampedModel):
    customer = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    status = models.CharField(max_length=10,  choices=STATUS_ORDER)

    def __str__(self):
        return f"{self.pk} - {self.customer} - {self.status}"

    @property
    def total(self):
        total = 0
        for od in self.order_details.all():
            total += od.total
        return total


class OrderDetail(TimeStampedModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_details"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_details"
    )
    quantity = models.IntegerField()

    @property
    def total(self):
        return self.product.price_product * self.quantity


class Invoice(TimeStampedModel):
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="invoice",
        null=False
    )
    code = models.CharField(max_length=20)
    date = models.DateTimeField('date creation')


class InvoiceDetail(TimeStampedModel):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="invoice_details",
        null=False
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="invoice_details"
    )
    quantity = models.IntegerField()


class Payment(TimeStampedModel):
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment"
    )
    date = models.DateTimeField('date payment')
    total = models.DecimalField(max_digits=10, decimal_places=3)
    tax = models.DecimalField(max_digits=10, decimal_places=3)

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.tax = 0
        self.total = 0
        self.date = datetime.datetime.now()
        for od in self.order.order_details.all():
            self.total += od.total

        result = super(Payment, self).save(*args, **kwargs)
        self.order.status = 'PAID'
        self.order.save()
        return result
