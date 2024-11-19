from django.db import models

# Clase Abstracta para registrar automáticamente la fecha de creación y actualización


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
