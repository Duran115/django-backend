from django.db import models

# Create your models here.

# Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

# Profesor
class Profesor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# Estudiante
class Estudiante(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)