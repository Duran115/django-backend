from django.contrib import admin
from .models import Calificacion

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'profesor', 'puntaje']

admin.site.register(Calificacion, CalificacionAdmin)