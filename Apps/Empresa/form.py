from django import forms

# importamos sistema de validacion
from django.core import validators

# importamos apliaciones
from Apps.Empresa.models import Empleado, Cargo


class CargoForm(forms.Form):
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(60)
    ],
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Ej. Administrador'
    }),
    label='Nombre:')


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre']

    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(60)
    ],
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Ej. Administrador'
    }),
    label='Nombre:')

# *--------------------------------

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(60)
    ],
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Ej. Alverto'
    }),
    label='Nombre:')
    
    correo = forms.EmailField()

    salario = forms.FloatField(validators=[
        validators.MinValueValidator(0)
    ],
    widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Ej. $500.000'
    }),
    label='Salario ($):')

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ['nombre','correo','salario']

    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(60)
    ],
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Ej. Alverto'
    }),
    label='Nombre:')

    correo = forms.EmailField()

    salario = forms.FloatField(validators=[
        validators.MinValueValidator(0)
    ],
    widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Ej. $500.000'
    }),
    label='Salario ($):')








