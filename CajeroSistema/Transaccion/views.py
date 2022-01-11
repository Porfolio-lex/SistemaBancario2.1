from django.shortcuts import render
from .models import Prueba, Person
from django.contrib.auth.models import User

# Create your views here.

#Created method crud Userse}
def Login(request):
    return render(request=request, template_name="Login.html")

def Datos(request):
    DatosObtenidos = Person.objects.all()
    print(DatosObtenidos)
    return render(request=request, template_name="Prueba.html", context={"Usuario":DatosObtenidos})

def Home(request):
    return render(request=request, template_name="Base.html")
    
def Registro(request):
    return render(request=request, template_name="Registros.html")
