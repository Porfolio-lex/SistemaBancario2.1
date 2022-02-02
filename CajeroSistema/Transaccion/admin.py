from django.contrib import admin
from .models import Prueba, Card, Person
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(Prueba)
admin.site.register(Person, UserAdmin)
admin.site.register(Card)