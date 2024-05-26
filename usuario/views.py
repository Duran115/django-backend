from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] != request.POST['password2']:
                return render(request, 'signup.html', {
                    'form': UserCreationForm, 
                    'error': 'Las contraseñas no coinciden.'
                    })
            user = Usuario.objects.create(
                email=request.POST['email'], 
                password=request.POST['password1'],
                nombre=request.POST['first_name'],
                apellidos=request.POST['last_name'],
                )
            user.save()
            return HttpResponse('Usuario registrado correctamente.')
        except Exception as e:
            return render(request, 'signup.html', {
                'form': UserCreationForm, 
                'error': str(e)
                })
    else:
        return render(request, 'signup.html', {
            'form': UserCreationForm
            })

def login(request):
    return render(request, 'login.html')
