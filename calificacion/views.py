from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CalificacionSerializer
from .models import Calificacion

class CalificacionViewSet(viewsets.ModelViewSet):
    serializer_class = CalificacionSerializer
    queryset = Calificacion.objects.all()