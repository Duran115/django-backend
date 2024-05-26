from django.db import models
from usuario.models import Usuario

class Estudiante(Usuario):
    universidad = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    ciclo = models.PositiveIntegerField(blank=False, null=False, choices=[(i, i) for i in range(1, 11)])
    codigo = models.CharField(max_length=8, unique=True)
    
    def cursos_matriculados(self):
        from matricula.models import Matricula
        return [matricula.curso for matricula in Matricula.objects.filter(estudiante=self)]
    
    def matricularse(self, curso):
        from matricula.models import Matricula
        if not Matricula.objects.filter(estudiante=self, curso=curso).exists():
            Matricula.objects.create(estudiante=self, curso=curso)
            return True
        return False
    
    def retirarse(self, curso):
        from matricula.models import Matricula
        matricula = Matricula.objects.filter(estudiante=self, curso=curso).first()
        if matricula:
            matricula.delete()
            return True
        return False
    
    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
