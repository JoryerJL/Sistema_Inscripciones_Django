from django.shortcuts import render

# Create your views here.
def lista_curso(request):
    return render(request, 'dashboard/cursos/lista_curso.html')
