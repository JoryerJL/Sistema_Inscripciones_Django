from django.shortcuts import render

# Create your views here.
def index_website(request):
    return render(request, 'website/index.html')

def detail_course(request):
    return render(request, 'website/detail_course.html')
