from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MatriculaSerializer
from .models import Matricula

class MatriculaViewSet(viewsets.ModelViewSet):
    serializer_class = MatriculaSerializer
    queryset = Matricula.objects.all()