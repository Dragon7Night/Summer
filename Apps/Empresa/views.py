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

# <-------------REST FRAMEWORK----------------------->

# Importacion de deradores de rest Frameworks
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status


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


# !================= VISTAS CRUD DE LA API CON Django Framework ==========================

# .===================|CRUD PARA EL EMPLEADO|=======================
# Funcion para MOSTRAR todos los empleados y CREAR un solo empleado
@api_view(['GET','POST'])
def empleadoDataApi(request):

    # MUESTRA TODOS LOS EMPLEADOS 
    if request.method == 'GET':
        empleadoObject = Empleado.objects.all()
        serializerData = EmpleadoSerializer(empleadoObject, many=True)
        return Response(serializerData.data)

    # CREA UN SOLO EMPLEADO
    if request.method == 'POST':
        serializerData = EmpleadoSerializer(data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response(serializerData.data, status=status.HTTP_201_CREATED)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)


# Funcion para MOSTRAR, EDITAR Y ELMINAR SOLO un empleado por PK
@api_view(['GET','PUT','DELETE'])
def empleadoCrudApi(request, pk):

    # Validacion simple de verificacion del objeto
    try:
        empleadoObject = Empleado.objects.get(pk=pk)

    except Empleado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Obtenemos todos los datos del objeto que concuerda con la PK
    if request.method == 'GET':
        serializerData = EmpleadoSerializer(empleadoObject)
        return Response(serializerData.data)
    
    # Editamos un empleado buscado y validamos su guardado
    if request.method == 'PUT':
        serializerData = EmpleadoSerializer(empleadoObject, data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response(serializerData.data)
        return Response(serializerData.error, status=status.HTTP_400_BAD_REQUEST)
    
    # Permite eliminar el empleado buscado por PK
    if request.method == 'DELETE':
        empleadoObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# .===================|CRUD PARA EL CARGO|=======================
# Funcion para MOSTRAR todos los cargos y CREAR un solo cargo
@api_view(['GET','POST'])
def cargoDataApi(request):

    # MUESTRA TODOS LOS CARGOS 
    if request.method == 'GET':
        cargoObject = Cargo.objects.all()
        serializerData = CargoSerializer(cargoObject, many=True)
        return Response(serializerData.data)

    # CREA UN SOLO CARGO
    if request.method == 'POST':
        serializerData = CargoSerializer(data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response(serializerData.data, status=status.HTTP_201_CREATED)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)


# Funcion para MOSTRAR, EDITAR Y ELMINAR SOLO un cargo por PK
@api_view(['GET','PUT','DELETE'])
def cargoCrudApi(request, pk):

    # Validacion simple de verificacion del objeto
    try:
        cargoObject = Cargo.objects.get(pk=pk)

    except Cargo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Obtenemos todos los datos del objeto que concuerda con la PK
    if request.method == 'GET':
        serializerData = CargoSerializer(cargoObject)
        return Response(serializerData.data)
    
    # Editamos un cargo buscado y validamos su guardado
    if request.method == 'PUT':
        serializerData = CargoSerializer(cargoObject, data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response(serializerData.data)
        return Response(serializerData.error, status=status.HTTP_400_BAD_REQUEST)
    
    # Permite eliminar el cargo buscado por PK
    if request.method == 'DELETE':
        cargoObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





































































