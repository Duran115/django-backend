from django.shortcuts import render
from rest_framework import viewsets
from .serializer import EstudianteSerializer
from .models import Estudiante

class EstudianteViewSet(viewsets.ModelViewSet):
    serializer_class = EstudianteSerializer
    queryset = Estudiante.objects.all()
