from django.db import models
from django.db.models.fields import AutoField, CharField
from django.contrib.auth.models import  AbstractUser, PermissionsMixin, User
from djongo import models as dj

# Create your models here.
class Prueba(models.Model):
    nombre = models.CharField(max_length=50)

class Card(models.Model):
    cardid = models.CharField(max_length=20)
    cardpasswd = models.CharField(max_length=20)
    cardmoney = models.CharField(max_length=20)
    carlock = models.CharField(max_length=20)

class Person(AbstractUser):
     name = models.CharField(primary_key=True, max_length=20)
     Cedula = models.CharField(max_length=20)
     Telefono = models.CharField(max_length=20)
     NumeroCuenta = models.CharField(max_length=20)
     #Modificamos el email para que sea unico, y asi poder iniciar sesión con el 
     email = models.EmailField(
        ("email address"),
        unique=True
     )
    #Agregamos como requerido el username y ponemos al email como field
     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = ["username"]