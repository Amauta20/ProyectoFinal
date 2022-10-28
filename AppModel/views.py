from django.shortcuts import render
from AppModel.models import Familiar
from AppModel.forms import Buscar
from django.views import View

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

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "AppModel/familiares.html", {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'AppModel/buscar.html'
    initial = {"nombres":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombres = form.cleaned_data.get("nombres")
            lista_familiares = Familiar.objects.filter(nombres__icontains=nombres).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})