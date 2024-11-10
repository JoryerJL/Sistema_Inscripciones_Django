
from django.urls import path, include
from .views import *

app_name = 'website'

urlpatterns = [
    path('', index_website, name='index'),
    path('detail_course/', detail_course, name='detail_course'),
    path('logout/', logout_view, name='logout_view'),
    path('registro_alumno/', registro_alumno, name='registro_alumno'),
]