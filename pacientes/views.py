from django.shortcuts import render, redirect, get_object_or_404
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
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
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
        lista_pacientes = self.model.objects.get_queryset().order_by('id')
        context["objects"] = lista_pacientes
        return context


# @login_required
# def lista_crear(request):
#     if request.method == 'POST':
#         form = PacienteCrearForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Paciente  creado!! ')
#             return redirect('pacientes:pacientes-listar')
#     else:
#         paciente_list = Paciente.objects.all()
#         paginator = Paginator(paciente_list, 5) # Show 25 contacts per page
#         page = request.GET.get('page')
#         pacientes = paginator.get_page(page)
#         form = PacienteCrearForm()
#     return render(request,'pacientes/pacientes_listar.html',{'form':form,'pacientes':pacientes})

@login_required
def listar_pacientes(request):
    paciente_list = Paciente.objects.all().order_by('apellido_paterno')
    paginator = Paginator(paciente_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    pacientes = paginator.get_page(page)
    return render(request,'pacientes/pacientes_listar.html',{'pacientes':pacientes})

@login_required
def paciente_crear(request):
    data = dict()

    if request.method == 'POST':
        form = PacienteCrearForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, f'Paciente  creado!! ')
            data['form_is_valid'] = True
            paciente_list = Paciente.objects.all().order_by('apellido_paterno')
            paginator = Paginator(paciente_list, 5) # Show 25 contacts per page
            page = request.GET.get('page')
            pacientes = paginator.get_page(page)
            
            data['html_pacientes_lista'] = render_to_string('pacientes/pacientes_parcial_listar.html', {
                'pacientes': pacientes,
                'message': {'message':'Paciente  creado!! ','tags':'success'}
            })
        else:
            data['form_is_valid'] = False
    else:
        form = PacienteCrearForm()

    context = {'form': form }
    data['html_form'] = render_to_string('pacientes/pacientes_crear.html',
        context,
        request=request,
    )
    return JsonResponse(data)

@login_required
def paciente_actualizar(request,pk):
    data = dict()
    paciente = get_object_or_404(Paciente,pk=pk)
    if request.method == 'POST':
        form = PacienteActualizarForm(request.POST,instance=paciente)
        if form.is_valid():
            form.save()
            #messages.success(request, f'Paciente  creado!! ')
            data['form_is_valid'] = True
            paciente_list = Paciente.objects.all().order_by('apellido_paterno')
            paginator = Paginator(paciente_list, 5) # Show 25 contacts per page
            page = request.GET.get('page')
            pacientes = paginator.get_page(page)
            data['html_pacientes_lista'] = render_to_string('pacientes/pacientes_parcial_listar.html', {
                'pacientes': pacientes,
                'message': {'message': f'Paciente { paciente.nombres } { paciente.apellido_paterno } { paciente.apellido_materno } Editado!! ', 'tags': 'success'}
            })
        else:
            data['form_is_valid'] = False
    else:

        form = PacienteActualizarForm(instance=paciente)

    context = {'form': form}
    data['html_form'] = render_to_string('pacientes/pacientes_update.html',
        context,
        request=request,
    )
    return JsonResponse(data)

@login_required
def paciente_buscar(request):
    data = dict()
    porte = len(request.GET['name'].split(' '))
    texto = request.GET['name'].split(' ',3)
    if (porte==1):
        apellido_paterno = texto[0]
        
        paciente = Paciente.objects.filter(Q(apellido_paterno__icontains=apellido_paterno) | Q(nombres__icontains=apellido_paterno) |  Q(rut__icontains=apellido_paterno)).order_by('apellido_paterno')
    elif (porte)==2:
        apellido_paterno = texto[0]
        apellido_materno = texto[1]
        paciente = Paciente.objects.filter(Q(apellido_paterno__icontains=apellido_paterno,apellido_materno__icontains=apellido_materno) | Q(nombres__icontains=apellido_paterno,apellido_paterno__icontains=apellido_materno)).order_by('apellido_paterno')
    elif (porte)==3:
        apellido_paterno = texto[0]
        apellido_materno = texto[1]
        nombres = texto[2]
        paciente = Paciente.objects.filter(Q(apellido_paterno__icontains=apellido_paterno,apellido_materno__icontains=apellido_materno,nombres__icontains=nombres) | Q(nombres__icontains=apellido_paterno,apellido_paterno__icontains=apellido_materno,apellido_materno__icontains=nombres)).order_by('apellido_paterno') 
    
    paginator = Paginator(paciente, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    pacientes = paginator.get_page(page)
    data['html_pacientes_lista'] = render_to_string('pacientes/pacientes_parcial_listar.html', {
        'pacientes': pacientes
    })
    return JsonResponse(data)

@login_required
def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    data = dict()
    if request.method == 'POST':
        paciente.delete()
        data['form_is_valid'] = True
        paciente_list = Paciente.objects.all().order_by('apellido_paterno')
        paginator = Paginator(paciente_list, 5) # Show 25 contacts per page
        page = request.GET.get('page')
        pacientes = paginator.get_page(page)
        data['html_pacientes_lista'] = render_to_string('pacientes/pacientes_parcial_listar.html', {
            'pacientes': pacientes
        })
    else:
        context = {'paciente': paciente}
        data['html_form'] = render_to_string('pacientes/pacientes_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

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
