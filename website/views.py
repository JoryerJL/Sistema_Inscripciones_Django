from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def index_website(request):
    return render(request, 'website/index.html')

def detail_course(request):
    return render(request, 'website/detail_course.html')

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
        'form': form
    }
    return render(request, 'registration/registro_alumno.html', context)
def logout_view(request):
    logout(request)
    return redirect('website:index')
