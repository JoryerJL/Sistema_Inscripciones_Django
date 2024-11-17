from django.contrib import admin
from .models import *

admin.site.register(Curso)
admin.site.register(CursoOfertado)
admin.site.register(EstatusCursoOfertado)
admin.site.register(CategoriaCurso)