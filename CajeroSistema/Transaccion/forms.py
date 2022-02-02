#from django.contrib.auth import forms1
from django.db.models import fields
from django import forms
from .models import Person
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = Person
        fields = [
                'first_name',
                'last_login',
                'last_name',
                'username',
                'email',
                'Cedula',
                'Telefono',
                'NumeroCuenta',
                'Saldo',
                'password1',
                'password2'
            ]
        Labels = {
                'first_name':'Nombres',
                'last_name':'Apellidos',
                'last_login':'last_login',
                'username':'Nombre de usuario',
                'email':'Correo',
                'Cedula':'Cedula',
                'Telefono':'Telefono',
                'NumeroCuenta':'NumeroCuenta',
                'Saldo':'Saldo',
                'password1':'password1',
                'password2':'password2'
        }

