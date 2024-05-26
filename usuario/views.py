from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils import timezone
from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

def inicio(request):
    return render(request, 'inicio.html')

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
            login(request, user)
        except IntegrityError:
            return render(request, 'signup.html', {
                'form': UserCreationForm, 
                'error': 'El email ya está registrado.',
                })
    else:
        return render(request, 'signup.html', {
            'form': UserCreationForm
            })

def signin(request):
    if request.method == 'POST':
        user = authenticate(request, correo=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(), 
                'error': 'Correo o contraseña incorrectos.'
            })
    else:
        return render(request, 'signin.html', {'form': AuthenticationForm()})

@login_required
def signout(request):
    logout(request)
    return redirect('inicio')