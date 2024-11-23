from django.db import models
from datetime import date, datetime

from share.models import TimeStampedModel

# Create your models here.

class Type_user(models.Model):
    name_type = models.CharField(max_length=50, verbose_name='Tipo Empleado')

    def __str__(self):
        return self.name_type
    
    class Meta:
     
        db_table = 'type_users'
        ordering = ['id']

class Users(models.Model):
    dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
    birthdate = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20, verbose_name='Nombre')
    surname = models.CharField(max_length=20, verbose_name='Apellido')
    phone_number = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.EmailField(max_length=54, verbose_name='Email')
    direction = models.CharField(max_length=250, verbose_name='Dirección')
    type_user = models.ForeignKey(Type_user, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
     
        db_table = 'users'
        ordering = ['id']

    