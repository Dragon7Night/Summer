from django.db import models

# Create your models here.


class Cargo(models.Model):

    # id no la definimos Django la gestiona
    nombre = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(models):
        return f'{models.nombre}'


class Empleado(models.Model):

    nombre = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    salario = models.FloatField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    # Relacion de ForeingKey con el model de Cargo
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(models):
        return f'{models.nombre} - {models.correo} - {models.salario} - {models.cargo}'




















