from django.urls import path
from django.conf import settings
from .views import (
    AgendaCreateView,
    agenda_crear_view,
    calendario_view,
    agenda_crear,
    agenda_crear_paciente,
    agenda_editar
)
app_name='agenda'
urlpatterns = [
    
    #path('new/<int:pk>', agenda_crear_view, name='agenda-crear'),
    path('new/<int:pk>', agenda_crear, name='agenda-crear'),
    path('calendario/', calendario_view, name='agenda-calendario'),
    path('calendario/new/', agenda_crear_paciente, name='agenda-crear-paciente'),
    path('calendario/editar/<int:pk>', agenda_editar, name='agenda-editar'),

]