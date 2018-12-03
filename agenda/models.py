from django.db import models
from django.urls import reverse
from pacientes.models import Paciente
# Create your models here.
class Hora(models.Model):
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        formatedHour = self.hora.strftime("%H:%M")
        return formatedHour
class Agenda(models.Model):
    nombre = models.CharField(max_length=70, blank=False)
    agenda_fecha = models.DateField(blank=False)
    hora_agenda =  models.ForeignKey(Hora, on_delete=models.CASCADE)
    agenda_creacion = models.DateField(auto_now=True)
    agenda_comentario = models.CharField(max_length=200, blank=False)
    agenda_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.agenda_fecha+' '+self.hora_agenda
    
    def get_absolute_url(self):
        return reverse('pacientes:pacientes-listar')