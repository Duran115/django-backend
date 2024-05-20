from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)

class Profesor(Usuario):
    especialización = models.CharField(max_length=255)
    horarios = models.ManyToManyField('Horario', related_name='profesores')

class Estudiante(Usuario):
    cursos = models.ManyToManyField('Curso', related_name='estudiantes')

class Horario(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='horarios')

class Asesoría(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='asesorías')
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, related_name='asesorías')
    estado = models.CharField(max_length=50)

class Examen(models.Model):
    nombre = models.CharField(max_length=255)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, related_name='examenes')
    fecha = models.DateField()
    subido_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='examenes')

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    profesores = models.ManyToManyField(Profesor, related_name='cursos')
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')
