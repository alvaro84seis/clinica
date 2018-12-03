from django.contrib import admin
from .models import Paciente, Sexo, Ciudad

admin.site.register(Paciente)
admin.site.register(Sexo)
admin.site.register(Ciudad)