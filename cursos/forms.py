from django import forms
from .models import *

class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'titulo',
            'descripcion',
            'categoria'
        ]


class CursoOfertadoModelForm(forms.ModelForm):
    class Meta:
        model = CursoOfertado
        fields = [
            'instructor',
            'precio',
            'fecha_inicio',
            'sede',
            'curso',
            'capacidad',
            'estatus'
        ]

        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'})
        }
