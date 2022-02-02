from typing_extensions import Required
from django.db import models
from django.db.models.fields import AutoField, CharField
from django.contrib.auth.models import  AbstractUser, PermissionsMixin, User
from djongo import models as modelsmongo

# Create your models here.
class Prueba(models.Model):
    nombre = models.CharField(max_length=50)

class Card(models.Model):
    cardid = models.CharField(max_length=20)
    cardpasswd = models.CharField(max_length=20)
    cardmoney = models.CharField(max_length=20)
    carlock = models.CharField(max_length=20)

class Person(AbstractUser):       
     _id = modelsmongo.ObjectIdField()
     Cedula = modelsmongo.IntegerField()
     Telefono = modelsmongo.IntegerField()
     NumeroCuenta = modelsmongo.IntegerField(null=True, blank=True)
     Saldo = modelsmongo.IntegerField()
     #Modificamos el email para que sea unico, y asi poder iniciar sesión con el 
     email = modelsmongo.EmailField(
        ("email address"),
        unique=True
     )
    #Agregamos como requerido el username y ponemos al email como field
     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = ["username"]