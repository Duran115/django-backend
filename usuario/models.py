from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10)

class Profesor(Usuario):
    especialización = models.CharField(max_length=255)
    horarios = models.ManyToManyField('asesorias.Horario', related_name='profesores')

class Estudiante(Usuario):
    cursos = models.ManyToManyField('cursos.Curso', related_name='estudiantes')
