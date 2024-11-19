from django.db import models
from users.models import Provider


STATUS_PRODUCT = [
    ('ACTIVATED', 'ACTIVATED'),
    ('BLOCK', 'BLOCK'),
    ('DISABLED', 'DISABLED'),
]


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


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
    price_product = models.DecimalField(max_digits=10, decimal_places=3)
    description_product = models.TextField
    status = models.CharField(max_length=15, choices=STATUS_PRODUCT)

    def __str__(self):
        return f"{self.name} ({self.status})"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        related_name="images",
        blank=False
    )
    # Instalar pilow
    # image = models.ImageField(
    #   upload_to=None, height_field=None, width_field=None, max_length=100)
