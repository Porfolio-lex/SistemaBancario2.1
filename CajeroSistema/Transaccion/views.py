import json, random
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import Prueba, Person
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm

# Create your views here.

#metodo de logeo
def LoginInit(request):
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        UserLog = authenticate(request, username=username, password= password)
        if(UserLog is not None):
            login(request, UserLog)
            return redirect (to = "/Home/")
        return render(request=request, template_name="Login.html", context={"error":"Fallo de autenticación"})
    return render(request=request, template_name="Login.html")

#Logout
def LogoIn(request):
    logout(request)
    return redirect (to="/login/")

#Crear Usuario
def AddPerson(request):
   
    NumerCardCreated = NumberCard() 
    form = RegistroForm(request.POST)
    valores = ''
    if form.is_valid():       
        user = form.save(commit=False)
        
        numbercard = user.NumeroCuenta = NumerCardCreated
        user.save()
        
        diccionario = {'NumeroCuenta': numbercard}
        return JsonResponse(diccionario)
    else:
        print("no es valido")
        user = form
        user.save()
    return JsonResponse(valores, safe=False)     
        
#Todos los usuarios        
def Datos(request):
    DatosObtenidos = Person.objects.all()
    return render(request=request, template_name="Prueba.html", context={"Usuario":DatosObtenidos})

#Pagina de Inicio
def Home(request):
    return render(request=request, template_name="Base.html")

#Pagina de Registros    
def Registro(request):
    return render(request=request, template_name="Registros.html")

#Crear Tarjeta aleatorio
def NumberCard():
    card = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10):
        randomnumber = random.randint(0,9)
        card[i] = randomnumber
    ListToTupla = tuple(card)
    TuplaToNumber = int(''.join(map(str,card)))
    
    return TuplaToNumber


#Transferir
def Transferir(request):
    return render(request=request, template_name="Transaccion.html")

def ProcesoTransferencia(request):
    
    cuentadeposita =request.POST["NumeroCuenta1"]
    cuentaRecibe = request.POST["NumeroCuenta2"]
    SaldoDepositado = request.POST["Saldo"]
        
    C1 = ObtenerCuentas(cuentadeposita)
    C2 = ObtenerCuentas(cuentaRecibe)
    
    SaldotoInt = int(SaldoDepositado)
    
    if(C1.Saldo> SaldotoInt):
        C1.Saldo = C1.Saldo - SaldotoInt
        C2.Saldo = C2.Saldo + SaldotoInt
        C1.save()
        C2.save()
    else: 
        diccionario = {'Error':'El Monto a retirar es mayor que su la cantidad en su cuenta'}
        return JsonResponse(diccionario)
        
    diccionario2 = {'SaldoActual':C1.Saldo, 'SaldoDebitar':SaldotoInt}  
    return JsonResponse(diccionario2)

#Buscar Cuentas    
def ObtenerCuentas(NumberCuenta):
    findcount = Person.objects.get(NumeroCuenta = NumberCuenta)
    return findcount    

#Proceso de retiro
def BuscarCuentas(request, cuenta):
    
    findcount = ObtenerCuentas(cuenta) 
     
    result = request.body.decode('utf-8')
    
    rex =json.loads(result)
    SaldoRetirar = int(rex["Retiro"])
    
    if(SaldoRetirar> findcount.Saldo):
        diccionario = {
            'Mensaje':'El Monto a retirar es mayor que su saldo actual',
            'status':500    
        }
        print("mistake")
        return JsonResponse(diccionario)
    else:
        findcount.Saldo = findcount.Saldo- SaldoRetirar
        findcount.save()
        print("success")
        diccionario = {
            'Mensaje':'El Saldo fue descontado',
            'status':200,
            'dat':{
                'SaldoActual':findcount.Saldo
            }
        }
        return JsonResponse(diccionario)
   

def Retiro(request):
    return render(request=request, template_name="Retirar.html")

def Deposito(request):
    return render(request=request, template_name="Deposito.html")

def Info(request):
    return render(request=request, template_name="Info.html")

def AddSaldo(request):
    
    CuentaRequest = request.POST["NumeroCuenta"]
    SaldoDeposita = request.POST["SaldoR"]
    
    AcctualyCount = ObtenerCuentas(CuentaRequest)
    SaldoInit = int(SaldoDeposita)
    
    AcctualyCount.Saldo = AcctualyCount.Saldo + SaldoInit
    AcctualyCount.save()
    respuesta = {
        'Mensaje':'!Saldo Agregado¡',
        'SaldoActual': AcctualyCount.Saldo
    }
    return JsonResponse(respuesta)
#Eliminar
def delete(request, cuentaN):
    
    CuentaDelete = Person.objects.get(NumeroCuenta=cuentaN) 
    CuentaDelete.delete()
    #CuentaDelete.save()
    return redirect(to="/ListaUsuarios/")