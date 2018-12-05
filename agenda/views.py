from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Agenda,EstadoAgenda
from .forms import AgendaCrearForm
from django.contrib import messages
from pacientes.models import Paciente

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
    return render(request,'agenda/agenda_crear.html',{'form':form})
