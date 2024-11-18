from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class User_proart(models.Model):
    user = models.OneToOneField(
        UserModel, null=False, blank=False, related_name='user_proart')


class Provider(models.Model):
    user_proart = models.OneToOneField(
        User_proart, null=False, blank=False, related_name='provider')
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=254)
    direccion = models.CharField(max_length=20)


class Customer(models.Model):
    user_proart = models.OneToOneField(
        User_proart, null=False, blank=False, related_name='customer')
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=254)
    direccion = models.CharField(max_length=20)
