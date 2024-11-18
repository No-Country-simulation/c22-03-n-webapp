from django.db import models

from user_proart.models import Provider


STATUS_PRODUCT = [
    ('Activated', 'Activated'),
    ('Block', 'Block'),
    ('Disabled', 'Disabled'),
]


class Category(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        null=False,
        related_name="products",
        blank=False)
    categories = models.ManyToManyField(Category, related_name="products")
    name = models.CharField(max_length=20)
    quantities = models.IntegerField(default=0)
    price_product = models.FloatField(max_length=10)
    description_product = models.TextField
    status = models.CharField(max_length=15, choices=STATUS_PRODUCT)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        related_name="images",
        blank=False
    )
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100)
