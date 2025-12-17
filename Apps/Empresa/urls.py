from django.contrib import admin
from django.urls import path

from Apps.Empresa.views import *

urlpatterns = [

    # URLS de Cargo -- CRUD de Django
    path('data-cargo/', dataCargo, name='data_cargo'),
    path('registrar-cargo/', registrarCargo, name='registrar_cargo'),
    path('editar-cargo/<int:id>', editarCargo, name='editar_cargo'),
    path('eliminar-cargo/<int:id>', eliminarCargo, name='eliminar_cargo'),

    # URLS de Empleado -- CRUD de Django
    path('data-empleado/', dataEmpleado, name='data_empleado'),
    path('registrar-empleado/', registrarEmpleado, name='registrar_empleado'),
    path('editar-empleado/<int:id>', editarEmpleado, name='editar_empleado'),
    path('eliminar-empleado/<int:id>', eliminarEmpleado, name='eliminar_empleado'),

    # URLS de Cargo -- CRUD de la Api
    path('data-cargo-api/', cargoDataApi, name='data_cargo_api'),
    path('crud-cargo-api/<int:pk>', cargoCrudApi, name='crud_cargo_api'),

    # URLS de Empleado -- CRUD de la Api
    path('data-empleado-api/', empleadoDataApi, name='data_empleado_api'),
    path('crud-empleado-api/<int:pk>', empleadoCrudApi, name='crud_empleado_api'),
]





