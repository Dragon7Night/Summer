from django.contrib import admin

from Apps.Empresa.models import Empleado, Cargo

# Register your models here.

# CRUD del administrador para Cargo 
class CargoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']

admin.site.register(Cargo, CargoAdmin)


# CRUD del administrador para el Empleado
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','correo','salario','cargo']

admin.site.register(Empleado, EmpleadoAdmin)



















