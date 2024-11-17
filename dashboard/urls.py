from django.urls import path
from django.views.generic import TemplateView
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/index.html'), name='dashboard'),
    path('lista-curso/', lista_curso, name='lista_curso'),
]