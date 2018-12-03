from django.urls import path
from django.conf import settings
from .views import (
    AgendaCreateView
)
app_name='agenda'
urlpatterns = [
    
    path('new/', AgendaCreateView.as_view(), name='agenda-crear'),
]