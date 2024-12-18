
from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

app_name = 'website'

urlpatterns = [
    path('', index_website, name='index'),
    path('detalle-curso/<int:pk>/', detail_course, name='detail_course'),
    path('logout/', logout_view, name='logout_view'),
    path('registro_alumno/', registro_alumno, name='registro_alumno'),
    path('pre-inscripcion/<int:pk>', preinscripcion_alumno, name='pre-inscripcion_course'),
    path('pre-inscripcion/edit/<int:pk>', edit_preinscripcion, name='edit-pre-inscripcion_course'),
    path('quienes-somos/', TemplateView.as_view(template_name='website/quienes_somos.html'), name='quienes_somos'),
    path('contacto/', TemplateView.as_view(template_name='website/contacto.html'), name='contacto')
]