from django.db import models
from estudiante.models import Estudiante
from curso.models import Curso

class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    fecha_matricula = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('estudiante', 'curso')
    
    def __str__(self):
        return f'{self.estudiante.nombre} matriculado en {self.curso.nombre}'
