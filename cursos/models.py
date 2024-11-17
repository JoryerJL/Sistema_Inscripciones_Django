from django.db import models

# Create your models here.
class Curso(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey('CategoriaCurso', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'curso'
        ordering = ['titulo']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class EstatusCursoOfertado(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'estatus_curso_ofertado'

    def __str__(self):
        return self.nombre


class CursoOfertado(models.Model):
    sedes = (
        (1, 'Plantel Centro'),
        (2, 'Plantel Tenosique'),
    )
    instructor = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_inicio = models.DateField(blank=True, null=True)
    sede = models.PositiveIntegerField(choices=sedes)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    capacidad = models.PositiveSmallIntegerField(default=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.ForeignKey(EstatusCursoOfertado , on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.curso.titulo} - {self.fecha_inicio}'

    class Meta:
        db_table = 'curso_ofertado'
        verbose_name = 'Curso Ofertado'
        verbose_name_plural = 'Cursos Ofertados'


class CategoriaCurso (models.Model) :
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria_curso'
