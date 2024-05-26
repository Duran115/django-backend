from django.db import models
from curso.models import Curso

class Horario(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='horarios')
    dia = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    def __str__(self):
        return f'{self.dia} {self.hora_inicio}-{self.hora_fin}'
