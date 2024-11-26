from django.db import models
from share.models import TimeStampedModel
from users.models import Customer
from products.models import Product

STATUS_ORDER = (
    ('CANCELED', 'CANCELED'),
    ('PENDING', 'PENDING'),
    ('INVOICED', 'INVOICED'),
)


class Order(TimeStampedModel):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    # date = models.DateTimeField('date creation')
    status = models.CharField(max_length=10,  choices=STATUS_ORDER)

    def __str__(self):
        return f"{self.pk} - {self.customer} - {self.status}"

    def save(self, *args, **kwargs):
        self.total = 0
        for od in self.order.order_details.all():
            self.total += od.total
        return super(Order, self).save(*args, **kwargs)


"""
select sum(pro.price * od.quantity)
from od, pro
where od.order.pk=3 and od.productpk=pro.pk

o = Order.objects.filter(pk=3).first()
o = Order.objects.get(pk=3)

o.order_details.all() --- lista de order detail
total = 0
for od in o.order_details.all():
    total += od.quantity * od.product.price_product

    
o.order_details.all().aggregate(total=Sum(F('quantity') * F('product__price_product')))
"""


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

    def save(self, *args, **kwargs):
        self.total = 0
        for od in self.order.order_details.all():
            self.total += od.total
        return super(Payment, self).save(*args, **kwargs)
