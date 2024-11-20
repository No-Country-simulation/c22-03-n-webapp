from django.db import models
from django.contrib.auth import get_user_model

from share.models import TimeStampedModel
UserModel = get_user_model()


class User_proart(TimeStampedModel):
    user = models.OneToOneField(
        UserModel,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='user_proart'
    )
    # UserModel tiene sus propios campos, como nombre, surname, email, etc.

    def __str__(self) -> str:
        return f"{self.pk} {self.user.username}"


class Provider(TimeStampedModel):
    user_proart = models.OneToOneField(
        User_proart,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='provider'
    )
    # Tipo texto, faltará validar el cambio a int
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    # creation_date = models.DateField("creation date")
    # Los siguientes campos son de UserModel)por lo que no hace falta declarlo
    # name = models.CharField(max_length=20)
    # surname = models.CharField(max_length=20)
    # email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.user_proart.user.email} - {self.user_proart.user.username} ({self.phone_number})"  # noqa


class Customer(TimeStampedModel):
    user_proart = models.OneToOneField(
        User_proart,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='customer'
    )
    # Tipo texto, faltará validar el cambio a int
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    # creation_date = models.DateField("creation date")
    # name = models.CharField(max_length=20)
    # surname = models.CharField(max_length=20)
    # email = models.EmailField(max_length=254)
