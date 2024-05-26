from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def estudiante(request):
    return HttpResponse('Estudiante')

def profesor(request):
    return HttpResponse('Profesor')