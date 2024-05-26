from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProfesorSerializer
from .models import Profesor

class ProfesorViewSet(viewsets.ModelViewSet):
    serializer_class = ProfesorSerializer
    queryset = Profesor.objects.all()