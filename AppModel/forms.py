from django import forms
from AppModel.models import Familiar

class Buscar(forms.Form):
    nombres = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombres', 'direccion', 'numero_pasaporte', 'nacimiento']
    