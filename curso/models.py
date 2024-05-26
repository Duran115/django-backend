from django.db import models
from profesor.models import Profesor

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')
    
    @property
    def estudiantes_matriculados(self):
        return [matricula.estudiante for matricula in self.matriculas.all()]
    
    def __str__(self):
        return self.nombre
