from django.urls import path
from django.conf import settings
from .views import (
    AgendaCreateView,
    agenda_crear_view,
    calendario_view,
    agenda_crear
)
app_name='agenda'
urlpatterns = [
    
    #path('new/<int:pk>', agenda_crear_view, name='agenda-crear'),
    path('new/<int:pk>', agenda_crear, name='agenda-crear'),
    path('calendario/', calendario_view, name='agenda-calendario'),

]