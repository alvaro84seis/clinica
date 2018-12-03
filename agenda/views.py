from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Agenda
from .forms import AgendaCrearForm
from django.contrib import messages
# Create your views here.

class AgendaCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Agenda
    form_class = AgendaCrearForm
    template_name = 'agenda/agenda_crear.html'
    success_message = 'Paciente Creado con Exito'
 