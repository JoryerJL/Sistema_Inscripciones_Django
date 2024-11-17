from django.db import models

# Create your models here.
class Curso(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    #precio = models.DecimalField(max_digits=8, decimal_places=2)
    #|fecha_inicio = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'curso'
        ordering = ['titulo']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'