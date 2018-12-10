from django.urls import path
from django.conf import settings
from .views import (
    AgendaCreateView,
    agenda_crear_view,
    calendario_view
)
app_name='agenda'
urlpatterns = [
    
    path('new/<int:id>', agenda_crear_view, name='agenda-crear'),
    path('calendario/', calendario_view, name='agenda-calendario'),

]