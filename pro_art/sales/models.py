from django.db import models
from user_proart.models import Customer
from product_proart.models import Product

STATUS_ORDER = (
    ('DRAFT', 'DRAFT'),
    ('PENDING', 'PENDING'),
    ('INVOICED', 'INVOICED'),
)


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name="orders")
    date = models.DateTimeField('date creation')
    status = models.CharField(choices=STATUS_ORDER)

    def __str__(self):
        return self.status


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name="order_details")
    product = models.ForeignKey(Product, related_name="order_details")
    quantity = models.IntegerField()


class Invoice(models.Model):
    order = models.OneToOneField(Order, related_name="invoice", null=False)
    code = models.CharField(max=20)
    date = models.DateTimeField('date creation')


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice, related_name="invoice_details", null=False)
    product = models.ForeignKey(Product, related_name="order_details")
    quantity = models.IntegerField()


class Payment(models.Model):
    invoice = models.OneToOneField(Invoice, related_name="payment")
    date = models.DateTimeField('date payment')
    total = models.DecimalField()
    tax = models.DecimalField()
