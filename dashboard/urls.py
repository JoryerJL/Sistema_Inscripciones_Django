from django.urls import path
from django.views.generic import TemplateView
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/index.html'), name='dashboard'),
    path('lista-curso/', lista_curso, name='lista_curso'),
    path('lista-preinscripcion/', lista_preinscripcion, name='lista_preinscripcion'),
    path('create-curso/', create_curso, name='create_curso'),
    path('create-curso-ofertado/', create_curso_ofertado, name='create_curso_ofertado'),
    path('delete-curso/<int:pk>/', delete_curso, name='delete_curso'),
    path('delete-curso-ofertado/<int:pk>/', delete_curso_Ofertado, name='delete_curso_ofertado'),

]