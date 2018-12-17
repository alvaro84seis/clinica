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
from django.template.loader import render_to_string
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
        #print("btn_ingresar_agenda")
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
        #query = Agenda.objects.filter( agenda_fecha__gte=time.strftime("%Y-%m-%d")).exclude(estado_agenda__id = 2)
        query = Agenda.objects.exclude(estado_agenda__id = 2)
        query = Agenda.objects.all()
        lista=[]
        for obj in query:
            #print(obj.estado_agenda.id)
            if obj.agenda_tipo.agenda_tipo == 'normal':

                color = "#FF0F0"
                textcolor="white"
            else:
                color = "yellow"
                textcolor="black"
            if obj.estado_agenda.id==2:
        
                color = "#F78181"
                textcolor="#D8D8D8"
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

@login_required
def agenda_crear(request,pk):
    data= dict()
    paciente2 = get_object_or_404(Paciente, pk=pk) 
    print(paciente2)
    if request.method=='POST':
        form = AgendaCrearForm(request.POST or None)
        if form.is_valid():

            estadoagenda = get_object_or_404(EstadoAgenda, id=1) 
            form.instance.estado_agenda=estadoagenda
            form.instance.agenda_paciente = paciente2
            print(form.cleaned_data)
            form.save()
            data['form_is_valid'] = True
            paciente_list = Paciente.objects.all().order_by('apellido_paterno')
            paginator = Paginator(paciente_list, 5) # Show 25 contacts per page
            page = request.GET.get('page')
            pacientes = paginator.get_page(page)
            
            data['html_pacientes_lista'] = render_to_string('pacientes/pacientes_parcial_listar.html', {
                'pacientes': pacientes,
                'message': {'message': f'Agenda para { paciente2.nombres } { paciente2.apellido_paterno } { paciente2.apellido_materno } Creada con EXITO!! ', 'tags': 'success'}
            })
        else:
            data['form_is_valid'] = False
    else:
        form=AgendaCrearForm()
        data['html_form']=render_to_string('agenda/agenda_crear.html', {
                'form': form,
                'paciente':paciente2
                 
            },request=request)
    return JsonResponse(data)

@login_required
def agenda_crear_paciente(request):
    data= dict()
    #print(paciente2)
    if request.method=='POST':
        form = AgendaCrearFormCalendario(request.POST or None)
        if form.is_valid():
            estadoagenda = get_object_or_404(EstadoAgenda, id=1) 
            form.instance.estado_agenda=estadoagenda
            #form.instance.agenda_paciente = paciente2
            #print(form.cleaned_data)
            form.save() 
            return redirect('agenda:agenda-calendario')   
    else:
        print( request.GET['agenda_fecha']  )
        form = AgendaCrearFormCalendario()
        data['html_form']=render_to_string('agenda/agenda_crear_paciente.html', {
                'form': form, 
                'agenda_fecha': str(request.GET['agenda_fecha'])  
            },request=request)
        return JsonResponse(data)

@login_required
def agenda_editar(request,pk):
    data= dict()
    
    agenda = get_object_or_404(Agenda,pk=pk)
    
    if request.method=='POST':
        form = AgendaEditarFormCalendario(request.POST or None,instance=agenda)
        if form.is_valid():
            form.save() 
            return redirect('agenda:agenda-calendario')   
    else:
        form = AgendaEditarFormCalendario(instance=agenda)
        data['html_form']=render_to_string('agenda/agenda_editar.html', {
                'form': form,'agenda':agenda  
            },request=request)
        return JsonResponse(data)

   
