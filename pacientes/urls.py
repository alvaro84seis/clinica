from django.urls import path
from .views import home_view
from django.conf import settings
from .views import (
    PacienteCreateView,
    PacienteListView,
    PacienteUpdateView,
    ListAndCreate
)
app_name= 'pacientes'
urlpatterns = [
    path('', home_view, name='pacientes_home'),
    path('new/', PacienteCreateView.as_view(), name='pacientes-crear'),
    path('listar/', ListAndCreate.as_view(), name='pacientes-listar'),
    path('listar/<int:pk>/update', PacienteUpdateView.as_view(), name='pacientes-actualizar'),
]
