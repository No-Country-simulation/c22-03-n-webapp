from django.db import models
from users.models import Provider
from share.models import TimeStampedModel

# Estados de los productos
STATUS_PRODUCT = [
    ('AVAILABLE', 'AVAILABLE'),
    ('BLOCK', 'BLOCK'),
    ('DISCONTINUED', 'DISCONTINUED'),
]

# Modelo de categorias
class Category(TimeStampedModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Modelo de productos
class Product(TimeStampedModel):
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

# Modelos de imagenes de productos
class ProductImage(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        related_name="images",
        blank=False
    )
    image = models.ImageField(
        null=True,
        blank=False,
        upload_to=None,
        height_field=None,
        width_field=None,
        max_length=100
    )

    def delete(self, *args, **kwargs):
        # TODO
        # remove file in disk
        return super().delete(*args, **kwargs)

# Modelo de proveedores
class Provider(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
