from lib2to3.fixes.fix_input import context
from pyexpat.errors import messages

from django.shortcuts import render
from cursos.models import *
from .forms import *

# Create your views here.
def perfil_alumno(request):
    messageSuccess = ''
    messageError = ''
    form = UserModelForm(instance=request.user)
    if request.method == 'POST':
        form = UserModelForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messageSuccess = 'Datos actualizados'
        else:
            messageError = form.errors
    cursos = PreinscripcionCurso.objects.filter(prospecto=request.user)
    context = {
        'cursos': cursos,
        'form': form,
        'messageSuccess': messageSuccess,
        'messageError': messageError

    }
    return render(request, 'usuarios/perfil_alumno.html', context)
