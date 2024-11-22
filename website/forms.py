from django import forms
from cursos.models import *

class InscripcionAlumnoCursoForm(forms.Form):
    comprobante_domicilio = forms.FileField()
    curp = forms.FileField()
    identificacion_oficial = forms.FileField()
    comprobante_pago = forms.FileField()
    comprobante_estudios = forms.FileField()
    acta_nacimiento = forms.FileField()

class PreInscripcionAlumnoCursoModelForm(forms.ModelForm):
    class Meta:
        model = PreinscripcionCurso
        fields  = [
            'comprobante_domicilio',
            'curp',
            'identificacion_oficial',
            'comprobante_pago',
            'comprobante_estudios',
            'acta_nacimiento'
        ]

