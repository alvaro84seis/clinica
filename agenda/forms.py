from django import forms
from .models import Agenda
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.contrib.admin import widgets 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import Textarea,SelectDateWidget
#import datetime,time
from datetime import datetime
from pacientes.models import Paciente

class AgendaCrearForm(forms.ModelForm):

    class Meta:
        now = datetime.now()
        model = Agenda
        #fields = ['rut','nombres','apellido_paterno','apellido_materno','sexo','fecha_nacimiento']
        exclude = ['agenda_creacion','agenda_paciente','estado_agenda']
        widgets = {
            'agenda_fecha': SelectDateWidget(attrs = {
                'placeholder': 'Ingrese fecha agenda',
                'data-date-format': 'dd/mm/yyyy',
                
                # added the class snps-inline-select
                'style':'width:auto;float:left',
                'class': 'form-control snps-inline-select'
            },years=range(now.year,+10))
            
        }
    def __init__(self, *args, **kwargs):
        super(AgendaCrearForm, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div('nombre','agenda_fecha','agenda_hora','agenda_comentario','agenda_tipo'),
            Div(
                Submit('ingresar', 'Ingresar', css_class="btn btn-outline-info"),
                HTML("<button class='btn btn-outline-secondary' data-dismiss='modal'>Cancelar</button>")
            )
         
        )
class AgendaCrearFormCalendario(forms.ModelForm):

    class Meta:
        now = datetime.now()
        model = Agenda

        #fields = ['rut','nombres','apellido_paterno','apellido_materno','sexo','fecha_nacimiento']
        exclude = ['agenda_creacion','estado_agenda']
        
        
    def __init__(self, *args, **kwargs):
        super(AgendaCrearFormCalendario, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div('agenda_paciente','agenda_hora','agenda_tipo','nombre','agenda_comentario',
                Field('agenda_fecha', type="hidden")
            ),
            Div(
                Submit('btn_ingresar_agenda', 'Ingresar', css_class="btn btn-outline-info"),
                HTML("<a class='btn btn-outline-secondary' href='' data-dismiss='modal'>Cancelar</a>")
            )
         
        )
class AgendaEditarFormCalendario(forms.ModelForm):

    class Meta:
        now = datetime.now()
        model = Agenda

        #fields = ['rut','nombres','apellido_paterno','apellido_materno','sexo','fecha_nacimiento']
        exclude = ['agenda_creacion']
        
        
    def __init__(self, *args, **kwargs):
        super(AgendaEditarFormCalendario, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div('nombre','agenda_hora','agenda_comentario','agenda_tipo','agenda_paciente','estado_agenda',
                Field('agenda_fecha', type="hidden")
            ),
            Div(
                Submit('btn_editar_agenda', 'Editar', css_class="btn btn-outline-info"),
                HTML("<a class='btn btn-outline-secondary' href='' data-dismiss='modal'>Cancelar</a>")
            )
         
        )