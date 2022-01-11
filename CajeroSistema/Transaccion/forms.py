#from django.contrib.auth import forms1
from django.db.models import fields
from django import forms
from .models import Person
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = Person
        fields = [
                'id',
                'first_name',
                'last_name',
                'username',
                'email',
                'Cedula',
                'Telefono',
                'NumeroCuenta',
                'password1',
                'password2'
            ]
        Labels = {
                'id':'id',
                'first_name':'Nombres',
                'last_name':'Apellidos',
                'username':'Nombre de usuario',
                'email':'Correo',
                'Perfil':'Perfiles',
                'Cedula':'Cedula',
                'Telefono':'Telefono',
                'NumeroCuenta':'NumeroCuenta',
                'password1':'password1',
                'password2':'password2'
        }

