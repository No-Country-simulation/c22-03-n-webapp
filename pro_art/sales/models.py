from django.db import models
from share.models import TimeStampedModel
from users.models import Users
from products.models import Product

STATUS_ORDER = (
    ('DRAFT', 'DRAFT'),
    ('PENDING', 'PENDING'),
    ('INVOICED', 'INVOICED'),
)


class Order(TimeStampedModel):
    customer = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    # date = models.DateTimeField('date creation')
    status = models.CharField(max_length=10,  choices=STATUS_ORDER)

    def __str__(self):
        return self.status


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
    invoice = models.OneToOneField(
        Invoice,
        on_delete=models.CASCADE,
        related_name="payment"
    )
    date = models.DateTimeField('date payment')
    total = models.DecimalField(max_digits=10, decimal_places=3)
    tax = models.DecimalField(max_digits=10, decimal_places=3)
