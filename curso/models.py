from django.db import models
from profesor.models import Profesor

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')
    
    def estudiantes_matriculados(self):
        from matricula.models import Matricula
        return [matricula.estudiante for matricula in Matricula.objects.filter(curso=self)]
    
    def __str__(self):
        return self.nombre
