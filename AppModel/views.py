from django.shortcuts import render

# Create your views here.

def saludo(request):
    return render(request, 'AppModel/saludar.html',
    {
        "nombre": "Steve",
        "apellido": "Chunga",
    }
)

def saludando(request, nombres, apellidos):
    return render(request, 'AppModel/saludar.html',
    {
        "nombre": nombres,
        "apellido": apellidos,
    }
)

def fnotas(request):
    return render(request, "AppModel/saludar.html", 
    {"notas":[1,2,3,4,5,6,7,8]}
)

def calcimc(request, peso, altura):
    imc=int(peso)/(int(altura)*int(altura))
    return render(request, "AppModel/imc.html", {'imc':imc})