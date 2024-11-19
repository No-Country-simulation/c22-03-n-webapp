from django.db import models
from django.contrib.auth import get_user_model
UserModel = get_user_model()


class User_proart(models.Model):
    user = models.OneToOneField(
        UserModel, null=False, blank=False, related_name='user_proart')
    # UserModel tiene sus propios campos, como nombre, surname, email, etc.


class Provider(models.Model):
    user_proart = models.OneToOneField(
        User_proart, null=False, blank=False, related_name='provider')
    phone_number = models.IntegerField(max_length=10)
    address = models.CharField(max_length=20)
    creation_date = models.DateField("creation date")
    # Los siguientes campos son de UserModel)por lo que no hace falta declarlo
    # name = models.CharField(max_length=20)
    # surname = models.CharField(max_length=20)
    # email = models.EmailField(max_length=254)


class Customer(models.Model):
    user_proart = models.OneToOneField(
        User_proart, null=False, blank=False, related_name='customer')
    phone_number = models.IntegerField(max_length=10)
    address = models.CharField(max_length=20)
    creation_date = models.DateField("creation date")
    # name = models.CharField(max_length=20)
    # surname = models.CharField(max_length=20)
    # email = models.EmailField(max_length=254)
