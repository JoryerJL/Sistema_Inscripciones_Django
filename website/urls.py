
from django.urls import path, include
from .views import *

app_name = 'website'

urlpatterns = [
    path('', index_website, name='index'),
    path('detail_course/', detail_course, name='detail_course'),
]