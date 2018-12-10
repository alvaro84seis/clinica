from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse,JsonResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Agenda,EstadoAgenda
from .forms import AgendaCrearForm,AgendaCrearFormCalendario,AgendaEditarFormCalendario
from django.contrib import messages
from pacientes.models import Paciente
import datetime,time,json
from django.core import serializers
from datetime import datetime
# Create your views here.

class AgendaCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Agenda
    form_class = AgendaCrearForm
    template_name = 'agenda/agenda_crear.html'
    success_message = 'Paciente Creado con Exito'


@login_required 
def agenda_crear_view(request, id):
    if request.method == 'POST':
        form = AgendaCrearForm(request.POST or None)
        if form.is_valid():
            paciente = get_object_or_404(Paciente, id=id) 
            form.instance.agenda_paciente = paciente
            estadoagenda = get_object_or_404(EstadoAgenda, id=1) 
            form.instance.estado_agenda=estadoagenda
            form.save()
            messages.success(request, 'Agenda Creada')
            return redirect('pacientes:pacientes-listar')
    else:
        form = AgendaCrearForm()
        paciente=get_object_or_404(Paciente, id=id) 
    return render(request,'agenda/agenda_crear.html',{'form':form,"paciente":paciente})

@login_required 
def calendario_view(request):
    if request.method == 'POST' and 'btn_ingresar_agenda' in request.POST:
        print("btn_ingresar_agenda")
        form = AgendaCrearFormCalendario(request.POST or None)
        if form.is_valid():
            estadoagenda = get_object_or_404(EstadoAgenda, id=1) 
            form.instance.estado_agenda=estadoagenda
            form.save()
            messages.success(request, 'Agenda Creada')  
            return redirect('agenda:agenda-calendario')
    else:
        print("GET")
        form = AgendaCrearFormCalendario()
        query = Agenda.objects.filter(agenda_fecha__gte=time.strftime("%Y-%m-%d"))
        lista=[]
        for obj in query:
            if obj.agenda_tipo.agenda_tipo == 'normal':
                color = "#FF0F0"
                textcolor="white"
            else:
                color = "yellow"
                textcolor="black"
            lista.append(
                {
                    "title": obj.nombre,
                    "id":obj.pk,
                    "start": datetime.strftime(obj.agenda_fecha, '%Y-%m-%d')+'T'+ obj.agenda_hora.hora.strftime("%H:%M"),
                    "color":color,
                    "textColor":textcolor
                }
            )
        return render(request,'agenda/agenda_calendario.html',{"json":json.dumps(lista),"form":form})
