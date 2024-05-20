from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10)

class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='profesor')
    especializacion = models.CharField(max_length=255)

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='estudiante')
