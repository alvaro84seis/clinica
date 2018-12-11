from django import forms
from .models import Paciente
from django.urls import reverse
from django.contrib.admin import widgets 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import Textarea,SelectDateWidget
import datetime

class PacienteCrearForm(forms.ModelForm):

    class Meta:
        now = datetime.datetime.now()
        model = Paciente
        #fields = ['rut','nombres','apellido_paterno','apellido_materno','sexo','fecha_nacimiento']
        exclude = ['fecha_ingreso']
        widgets = {
            'fecha_nacimiento': SelectDateWidget(attrs = {
                'placeholder': 'Ingrese fecha de nacimiento',
                'data-date-format': 'dd/mm/yyyy',
                # added the class snps-inline-select
                'style':'width:auto;float:left',
                'class': 'form-control snps-inline-select'
            },years=range(now.year,1910,-1)),
            'motivo_consulta': Textarea()
        }
    def __init__(self, *args, **kwargs):
        super(PacienteCrearForm, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_id = 'id_crear_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = "new/"
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div('rut','nombres'),
            Div(
                Div('apellido_paterno',css_class='col-md-6'),
                Div('apellido_materno',css_class='col-md-6'),
                css_class='row'
            ),
            Div(
                Div('sexo',css_class='col-md-6'),
                Div('fecha_nacimiento',css_class='col-md-6'),
                css_class='row'
            ),
            Div(
                Div('ciudad',css_class='col-md-6'),
                Div('email',css_class='col-md-6'),
                css_class='row'
            ),
            Div('direccion', 'motivo_consulta'),
            Div(
                Submit('ingresar', 'Ingresar', css_class="btn btn-outline-info"),
                HTML("<button class='btn btn-outline-secondary' data-dismiss='modal'>Cancelar</button>")
            )
         
        )

class PacienteActualizarForm(forms.ModelForm):

    class Meta:
        now = datetime.datetime.now()
        model = Paciente
        #fields = ['rut','nombres','apellido_paterno','apellido_materno','sexo','fecha_nacimiento']
        exclude = ['fecha_ingreso']
        widgets = {
            'fecha_nacimiento': SelectDateWidget(attrs = {
                'placeholder': 'Ingrese fecha de nacimiento',
                'data-date-format': 'dd/mm/yyyy',
                # added the class snps-inline-select
                'style':'width:auto;float:left',
                'class': 'form-control snps-inline-select'
            },years=range(now.year,1910,-1)),
            'motivo_consulta': Textarea()
        }
    def __init__(self, *args, **kwargs):
        super(PacienteActualizarForm, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div('rut','nombres'),
            Div(
                Div('apellido_paterno',css_class='col-md-6'),
                Div('apellido_materno',css_class='col-md-6'),
                css_class='row'
            ),
            Div(
                Div('sexo',css_class='col-md-6'),
                Div('fecha_nacimiento',css_class='col-md-6'),
                css_class='row'
            ),
            Div(
                Div('ciudad',css_class='col-md-6'),
                Div('email',css_class='col-md-6'),
                css_class='row'
            ),
            Div('direccion', 'motivo_consulta'),
            Div(
                Submit('actualizar', 'Actualizar', css_class="btn btn-outline-info"),
                HTML("<button class='btn btn-outline-secondary' data-dismiss='modal'>Cancelar</button>")
            )
         
        )
    