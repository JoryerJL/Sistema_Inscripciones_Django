from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from cursos.models import *


# Create your views here.
def lista_curso(request):
    cursos = CursoOfertado.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'dashboard/cursos/lista_curso.html', context)

def lista_preinscripcion(request):
    preinscripciones = PreinscripcionCurso.objects.all()
    context = {
        'preinscripciones': preinscripciones
    }
    return render(request, 'dashboard/cursos/lista_preinscripcion.html', context)
