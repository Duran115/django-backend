from django.db import models
from estudiante.models import Estudiante
from profesor.models import Profesor

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='puntuaciones')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='puntuaciones')
    puntaje = models.PositiveIntegerField(default=0, blank=False, null=False, choices=[(i, i) for i in range(11)])
    
    class Meta:
        unique_together = ('estudiante', 'profesor')
        
    def __str__(self):
        return f'Calificación de {self.estudiante} a {self.profesor}: {self.puntaje}'
