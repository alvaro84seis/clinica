from django.db import models
from django.urls import reverse
# Create your models here.
class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nombre_ciudad

class Sexo(models.Model):
    nombre_sexo = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nombre_sexo

class Paciente(models.Model):
    rut = models.CharField(max_length=11, blank=False, unique=True)
    nombres = models.CharField(max_length=60, blank=False)
    apellido_paterno = models.CharField(max_length=50, blank=False)
    apellido_materno = models.CharField(max_length=50, blank=False)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(blank=False)
    fecha_ingreso = models.DateField(auto_now=True)
    email = models.EmailField()
    direccion = models.CharField(max_length=100, blank=False)
    motivo_consulta = models.CharField(max_length=200, blank=False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.apellido_paterno+' '+self.apellido_materno+' '+self.nombres
    
    def get_absolute_url(self):
        return reverse('pacientes:pacientes-listar')