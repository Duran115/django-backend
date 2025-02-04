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
    return render(request, 'signup.html')

def signup_estudiante(request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] != request.POST['password2']:
                return render(request, 'signup_estudiante.html', {
                    'form': UserCreationForm, 
                    'error': 'Las contraseñas no coinciden.'
                    })
            from ..estudiante.models import Estudiante
            estudiante = Estudiante.objects.create(
                correo=request.POST['email'], 
                password=request.POST['password1'],
                nombre=request.POST['first_name'],
                apellidos=request.POST['last_name'],
                universidad = request.POST['universidad'],
                carrrera = request.POST['carrrera'],
                ciclo = request.POST['ciclo'],
                codigo = request.POST['codigo'],
                )
            estudiante.save()
            login(request, estudiante)
        except IntegrityError:
            return render(request, 'signup_estudiante.html', {
                'form': UserCreationForm, 
                'error': 'El email ya está registrado.',
                })
    else:
        return render(request, 'signup_estudiante.html', {'form': UserCreationForm})

def signup_profesor(request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] != request.POST['password2']:
                return render(request, 'signup_profesor.html', {
                    'form': UserCreationForm, 
                    'error': 'Las contraseñas no coinciden.'
                    })
            from ..profesor.models import Profesor
            profesor = Profesor.objects.create(
                correo=request.POST['email'], 
                password=request.POST['password1'],
                nombre=request.POST['first_name'],
                apellidos=request.POST['last_name'],
                profesion = request.POST['profesion'],
                centro_laboral = request.POST['centro_laboral'],
                )
            profesor.save()
            login(request, profesor)
        except IntegrityError:
            return render(request, 'signup_profesor.html', {
                'form': UserCreationForm, 
                'error': 'El email ya está registrado.',
                })
    else:
        return render(request, 'signup_profesor.html', {'form': UserCreationForm})

def signin(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['password']
        
        from estudiante.models import Estudiante
        from profesor.models import Profesor
        # Verificar si el correo pertenece a un Estudiante
        try:
            estudiante = Estudiante.objects.get(correo=correo)
            user = authenticate(request, correo=correo, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
        except Estudiante.DoesNotExist:
            pass
        # Verificar si el correo pertenece a un Profesor
        try:
            profesor = Profesor.objects.get(correo=correo)
            user = authenticate(request, correo=correo, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
        except Profesor.DoesNotExist:
            pass
        return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Correo o contraseña incorrectos.'})
    return render(request, 'signin.html', {'form': AuthenticationForm})


@login_required
def signout(request):
    logout(request)
    return redirect('inicio')