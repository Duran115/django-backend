from django.contrib import admin
from .models import Horario

class HorarioAdmin(admin.ModelAdmin):
    list_display = ['curso', 'dia', 'hora_inicio', 'hora_fin']

admin.site.register(Horario, HorarioAdmin)