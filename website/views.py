from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
def index_website(request):
    return render(request, 'website/index.html')

def detail_course(request):
    return render(request, 'website/detail_course.html')

def logout_view(request):
    logout(request)
    return redirect('website:index')
