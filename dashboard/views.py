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

def update_curso(request, pk):
    curso = Curso.objects.get(pk = pk)
    form = CursoModelForm(instance=curso)
    if request.method == 'POST':
        form = CursoModelForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('dashboard:lista_curso')
        else:
            print(form.errors)

    context = {
        'title': 'Editar Curso',
        'form': form
    }
    return render(request, 'dashboard/cursos/create_curso.html', context)

def update_curso_ofertado(request, pk):
    cursoOfertado = CursoOfertado.objects.get(pk = pk)
    form = CursoOfertadoModelForm(instance=cursoOfertado)
    if request.method == 'POST':
        form = CursoOfertadoModelForm(request.POST, instance=cursoOfertado)
        if form.is_valid():
            form.save()
            return redirect('dashboard:lista_curso')
        else:
            print(form.errors)

    context = {
        'title': 'Editar Curso Ofertado',
        'form': form
    }
    return render(request, 'dashboard/cursos/create_cursoOfertado.html', context)

def delete_curso(request, pk):
    Curso.objects.get(pk = pk).delete()
    return redirect('dashboard:lista_curso')

def delete_curso_Ofertado(request, pk):
    CursoOfertado.objects.get(pk = pk).delete()
    return redirect('dashboard:lista_curso')

def edit_preinscripcion(request, pk):
    preinscripcion = PreinscripcionCurso.objects.get(pk = pk)
    form = PreinscripcionCursoModelForm(instance=preinscripcion)
    if request.method == 'POST':
        form = PreinscripcionCursoModelForm(request.POST, instance=preinscripcion)
        if form.is_valid():
            form.save()
            return redirect('dashboard:lista_preinscripcion')
        else:
            print(form.errors)

    context = {
        'title': 'Editar Preinscripcion',
        'form': form,
        'preinscripcion' : preinscripcion
    }
    return render(request, 'dashboard/cursos/edit_preinscripcion.html', context)

def aceptar_preinscripcion(request, pk):
    preinscripcion = PreinscripcionCurso.objects.get(pk = pk)
    course = preinscripcion.curso
    preinscripcion.estatus = EstatusPreinscripcion.objects.get(pk=2)
    preinscripcion.save()
    if PreinscripcionCurso.objects.filter(curso=course, estatus_id=2).count() >= course.capacidad:
        course.estatus = EstatusCursoOfertado.objects.get(pk=4)
        course.save()
    return redirect('dashboard:lista_preinscripcion')

def rechazar_preinscripcion(request, pk):
    preinscripcion = PreinscripcionCurso.objects.get(pk = pk)
    course = preinscripcion.curso
    preinscripcion.estatus = EstatusPreinscripcion.objects.get(pk=3)
    preinscripcion.save()
    if not PreinscripcionCurso.objects.filter(curso=course, estatus_id=2).count() >= course.capacidad:
        course.estatus = EstatusCursoOfertado.objects.get(pk=1)
        course.save()
    return redirect('dashboard:lista_preinscripcion')