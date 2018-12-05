from django import forms
from .models import Agenda
from django.contrib.admin import widgets 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import Textarea,SelectDateWidget
import datetime

class AgendaCrearForm(forms.ModelForm):

    class Meta:
        now = datetime.datetime.now()
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
    