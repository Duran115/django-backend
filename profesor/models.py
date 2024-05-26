from django.db import models
from usuario.models import Usuario
from django.db.models import Avg

class Profesor(Usuario):
    profesion = models.CharField(max_length=100)
    centro_laboral = models.CharField(max_length=100)
    
    def cursos_creados(self):
        from curso.models import Curso
        return list(Curso.objects.filter(profesor=self))
    
    @property
    def puntuacion(self):
        avg_puntuacion = self.calificaciones.aggregate(Avg('puntaje'))['puntaje__avg']
        return avg_puntuacion if avg_puntuacion is not None else 0
    
    def crear_curso(self, nombre, descripcion):
        from curso.factories import CursoConcreteFactory
        factory = CursoConcreteFactory()
        curso = factory.crear_curso(nombre, descripcion, self)
        return curso
    
    def crear_horario(self, curso, dia, hora_inicio, hora_fin):
        from horario.factories import HorarioConcreteFactory
        factory = HorarioConcreteFactory()
        return factory.crear_horario(curso, dia, hora_inicio, hora_fin)
    
    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
