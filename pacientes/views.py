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
from .models import Paciente
from .forms import PacienteCrearForm, PacienteActualizarForm
from django.contrib import messages
# Create your views here.
@login_required
def home_view(request):
    return render(request,'pacientes/pacientes_home.html',{})

class PacienteCreateView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteCrearForm
    template_name = 'pacientes/pacientes_crear.html'
    success_message = 'Paciente Creado con Exito'
    
class ListAndCreate(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Paciente
    template_name = "pacientes/pacientes_listar.html"
    form_class = PacienteCrearForm
    success_message = 'Paciente Creado con Exito'
    def get_context_data(self, **kwargs):
        context = super(ListAndCreate, self).get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context

class PacienteListView(LoginRequiredMixin,ListView):
    model = Paciente
    template_name = 'pacientes/pacientes_listar.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'pacientes' 

class PacienteUpdateView(SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteActualizarForm
    template_name = 'pacientes/pacientes_update.html'  # <app>/<model>_<viewtype>.html
    def form_valid(self, form):
        messages.add_message(
               self.request, messages.SUCCESS, f"Usuario Actualizado { form.cleaned_data['rut']  }")
        return super(PacienteUpdateView, self).form_valid(form)