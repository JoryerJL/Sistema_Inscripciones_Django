from lib2to3.fixes.fix_input import context

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
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

def inscripcion_alumno(request):
    form = InscripcionAlumnoCursoForm()
    if request.method == "POST":
        form = InscripcionAlumnoCursoForm(request.POST, request.FILES)

    context = {
        'form': form
    }
    return render(request, 'website/inscripcion_course.html', context)

class InscripcionAlumno(TemplateView):
    template_name = 'website/inscripcion_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = InscripcionAlumnoCursoForm()
        context['form'] = form
        return context