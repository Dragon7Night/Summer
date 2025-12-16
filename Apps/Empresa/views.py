from django.shortcuts import render, get_object_or_404

# Importaciones para redireccionamiento
from django.http import HttpResponseRedirect
from django.urls import reverse


# Importaciones de los elementos [Modelos, Formularios y Serializadores]
from Apps.Empresa.models import Empleado, Cargo
from Apps.Empresa.form import EmpleadoForm, CargoForm
from Apps.Empresa.serializer import EmpleadoSerializer, CargoSerializer

# Importacion de decoradores
from django.contrib.auth.decorators import login_required

# ------------------------------------------------------------------

# Vista del Home de la pagina
def homeMain(request):
    return render(request, 'index.html')

# !=================VISTAS CRUD DE DJANGO==========================

# .=========Vista de cargo

# Devuelve todos los datos de la tabla Cargo
@login_required(login_url='')
def dataCargo(request):
    cargoObject = Cargo.objects.all()
    data = {'CargoKey':cargoObject}

    return render(request, 'xxxxxxxx.html', data)


# Muestra y registra los datos en el formulario de Cargo
def registrarCargo(request):
    formCargo = CargoForm()

    if request.method == 'POST':
        formCargo = CargoForm(request.POST)
        if formCargo.is_valid():
            formCargo.save()

            return HttpResponseRedirect(reverse('xxxxxxx'))
        
    data = {'formKey':formCargo}
    return render(request, 'xxxxx.html', data)


# Permite editar un cargo por ID
def editarCargo(request, id_cargo):
    cargoObject = get_object_or_404(Cargo, id=id_cargo)
    formCargo = CargoForm(instance=cargoObject)

    if request.method == 'POST':
        formCargo = CargoForm(request.POST, instance=cargoObject)
        if formCargo.is_valid():
            formCargo.save()
            return HttpResponseRedirect(reverse('xxxxxx'))
    
    data = {'formKey':formCargo}
    return render(request, 'xxxxxxxx.html', data)


# Permite eliminar un Cargo por ID
def eliminarCargo(request, id_cargo):
    cargoObject = get_object_or_404(Cargo, id=id_cargo)
    cargoObject.delete()

    return HttpResponseRedirect(reverse('xxxxxxxx'))

# .=========Vista de Empleado


# Devuelve todos los datos de la tabla Empleado
@login_required(login_url='')
def dataEmpleado(request):
    empleadoObject = Empleado.objects.all()
    data = {'EmpleadoKey':empleadoObject}

    return render(request, 'xxxxxxxx.html', data)


# Muestra y registra los datos en el formulario de Empleado
def registrarEmpleado(request):
    formEmpleado = EmpleadoForm()

    if request.method == 'POST':
        formEmpleado = EmpleadoForm(request.POST)
        if formEmpleado.is_valid():
            formEmpleado.save()

            return HttpResponseRedirect(reverse('xxxxxxx'))
        
    data = {'formKey':formEmpleado}
    return render(request, 'xxxxx.html', data)


# Permite editar un Cargp por ID
def editarEmpleado(request, id_empleado):
    empleadoObject = get_object_or_404(Empleado, id=id_empleado)
    formEmpleado = EmpleadoForm(instance=empleadoObject)

    if request.method == 'POST':
        formEmpleado = EmpleadoForm(request.POST, instance=empleadoObject)
        if formEmpleado.is_valid():
            formEmpleado.save()
            return HttpResponseRedirect(reverse('xxxxxx'))
    
    data = {'formKey':formEmpleado}
    return render(request, 'xxxxxxxx.html', data)


# Permite eliminar un Empleado por ID
def eliminarEmpleado(request, id_empleado):
    empleadoObject = get_object_or_404(Empleado, id=id_empleado)
    empleadoObject.delete()

    return HttpResponseRedirect(reverse('xxxxxxxx'))




































