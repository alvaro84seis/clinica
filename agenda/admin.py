from django.contrib import admin
from .models import Agenda,Hora,EstadoAgenda

admin.site.register(Agenda)
admin.site.register(Hora)
admin.site.register(EstadoAgenda)