from django.urls import path
from .views import home_view
from django.conf import settings
from .views import (
    PacienteCreateView,
    PacienteListView,
    PacienteUpdateView,
    ListAndCreate,
    listar_pacientes,
    paciente_crear,
    paciente_actualizar,
    paciente_delete,
    paciente_buscar
)
app_name= 'pacientes'
urlpatterns = [
    path('', home_view, name='pacientes_home'),
    #path('new/', PacienteCreateView.as_view(), name='pacientes-crear'),
    path('listar/new/', paciente_crear, name='pacientes-crear'),
    path('listar/', listar_pacientes, name='pacientes-listar'),
    path('listar/buscar/', paciente_buscar, name='pacientes-buscar'),
    #path('listar/', ListAndCreate.as_view(), name='pacientes-listar'),
    #path('listar/<int:pk>/update', PacienteUpdateView.as_view(), name='pacientes-actualizar'),
    path('listar/<int:pk>/update', paciente_actualizar, name='pacientes-actualizar'),
    path('listar/<int:pk>/delete', paciente_delete, name='pacientes-delete'),
]
