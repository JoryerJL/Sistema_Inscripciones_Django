from django.shortcuts import render

# Create your views here.
def perfil_alumno(request):
    return render(request, 'usuarios/perfil_alumno.html')
