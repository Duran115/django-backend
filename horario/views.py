from django.shortcuts import render
from rest_framework import viewsets
from .serializer import HorarioSerializer
from .models import Horario

class HorarioViewSet(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer
    queryset = Horario.objects.all()