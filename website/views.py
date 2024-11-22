from lib2to3.fixes.fix_input import context

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.views.generic import TemplateView
from .forms import *
from cursos.models import *


# Create your views here.
def index_website(request):
    course_list = CursoOfertado.objects.filter(estatus=1)
    context = {
        'course_list': course_list,
        'title' : 'Academy'
    }
    return render(request, 'website/index.html', context)

def detail_course(request, pk):
    course = CursoOfertado.objects.get(pk=1)
    context = {
        'course': course,
        'title' : course.curso.titulo
    }
    return render(request, 'website/detail_course.html', context)

def registro_alumno(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    context = {
        'form': form,
        'title' : 'Registro de Alumno'
    }
    return render(request, 'registration/registro_alumno.html', context)
def logout_view(request):
    logout(request)
    return redirect('website:index')

def preinscripcion_alumno(request, pk):
    course = CursoOfertado.objects.get(pk=pk)
    form = PreInscripcionAlumnoCursoModelForm()
    if request.method == "POST":
        form = PreInscripcionAlumnoCursoModelForm(request.POST, request.FILES)
        if form.is_valid():
            curso_temp = form.save(commit=False)
            curso_temp.prospecto = request.user
            curso_temp.curso = course
            curso_temp.estatus_id = 1
            curso_temp.save()
            print('Preinscripcion guardada')
            return redirect('website:index')

    context = {
        'form': form,
        'title': 'Pre-Inscripcion - ' + course.curso.titulo,
        'course': course
    }
    return render(request, 'website/inscripcion_course.html', context)

class InscripcionAlumno(TemplateView):
    template_name = 'website/inscripcion_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = InscripcionAlumnoCursoForm()
        context['form'] = form
        return context