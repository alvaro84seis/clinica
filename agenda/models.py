from django.db import models
from django.urls import reverse
from pacientes.models import Paciente
# Create your models here.
class Hora(models.Model):
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        formatedHour = self.hora.strftime("%H:%M")
        return formatedHour

class EstadoAgenda(models.Model):
    estado_agenda = models.CharField(max_length=70, blank=False)
    def __str__(self):
        return self.estado_agenda

class AgendaTipo(models.Model):
    agenda_tipo = models.CharField(max_length=70, blank=False)
    def __str__(self):
        return self.agenda_tipo

class Agenda(models.Model):
    nombre = models.CharField(max_length=70, blank=False)
    agenda_fecha = models.DateField(blank=False)
    agenda_hora =  models.ForeignKey(Hora, on_delete=models.CASCADE)
    agenda_creacion = models.DateField(auto_now=True)
    agenda_comentario = models.CharField(max_length=200, blank=False)
    agenda_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    estado_agenda = models.ForeignKey(EstadoAgenda, on_delete=models.CASCADE)
    agenda_tipo = models.ForeignKey(AgendaTipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('pacientes:pacientes-listar')