from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from cursos.models import *

# Create your views here.
def perfil_alumno(request):
    cursos = PreinscripcionCurso.objects.filter(prospecto=request.user)
    context = {
        'cursos': cursos
    }
    return render(request, 'usuarios/perfil_alumno.html', context)
