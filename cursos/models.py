from django.db import models

# # Create your models here.
# class Curso(models.Model):
#     nombre = models.CharField(max_length=255)
#     periodo = models.ForeignKey('Periodo', on_delete=models.CASCADE, related_name='cursos')
#     seccion = models.ForeignKey('Seccion', on_delete=models.CASCADE, related_name='cursos')
#     nivel = models.ForeignKey('Nivel', on_delete=models.CASCADE, related_name='cursos')
#     carrera = models.ForeignKey('Carrera', on_delete=models.CASCADE, related_name='cursos')

# class Periodo(models.Model):
#     codigo = models.CharField(max_length=10)

# class Seccion(models.Model):
#     codigo = models.CharField(max_length=10)

# class Nivel(models.Model):
#     numero = models.IntegerField()

# class Carrera(models.Model):
#     nombre = models.CharField(max_length=100)
