from django import forms

# importamos sistema de validacion
from django.core import validators

# importamos apliaciones
from Apps.Empresa.models import Empleado, Cargo



class CargoForm(forms.Form):
    nombre = forms.CharField()


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre']

    nombre = forms.CharField()

# *--------------------------------

class EmpleadoForm(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()
    salario = forms.FloatField()

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ['nombre','correo','salario']

    nombre = forms.CharField()
    correo = forms.EmailField()
    salario = forms.FloatField()








