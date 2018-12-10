from django.contrib import admin
from .models import Agenda,Hora,EstadoAgenda,AgendaTipo

admin.site.register(Agenda)
admin.site.register(Hora)
admin.site.register(EstadoAgenda)
admin.site.register(AgendaTipo)