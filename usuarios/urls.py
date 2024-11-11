from django.urls import path
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('perfil/alumno', perfil_alumno, name='perfil_alumno'),
]