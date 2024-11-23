from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from cursos.forms import *

from cursos.models import *


# Create your views here.
def lista_curso(request):
    cursos = Curso.objects.all()
    cursosOfertados = CursoOfertado.objects.all()
    context = {
        'cursos': cursos,
        'cursosOfertados': cursosOfertados
    }
    return render(request, 'dashboard/cursos/lista_curso.html', context)

def lista_preinscripcion(request):
    preinscripciones = PreinscripcionCurso.objects.all()
    context = {
        'preinscripciones': preinscripciones
    }
    return render(request, 'dashboard/cursos/lista_preinscripcion.html', context)

def create_curso(request):
    form = CursoModelForm()
    if request.method == 'POST':
        form = CursoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:lista_curso')
        else:
            print(form.errors)

    context = {
        'title': 'Nuevo Curso Ofertado',
        'form': form
    }
    return render(request, 'dashboard/cursos/create_curso.html', context)

def create_curso_ofertado(request):
    form = CursoOfertadoModelForm()
    if request.method == 'POST':
        form = CursoOfertadoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:lista_curso')
        else:
            print(form.errors)

    context = {
        'title': 'Nuevo Curso Ofertado',
        'form': form
    }
    return render(request, 'dashboard/cursos/create_cursoOfertado.html', context)

def delete_curso(request, pk):
    Curso.objects.get(pk = pk).delete()
    return redirect('dashboard:lista_curso')

def delete_curso_Ofertado(request, pk):
    CursoOfertado.objects.get(pk = pk).delete()
    return redirect('dashboard:lista_curso')