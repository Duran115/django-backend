from django.contrib import admin
from .models import Profesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['correo', 'nombre', 'apellidos', 'profesion', 'centro_laboral', 'cursos_creados']
    
    def cursos_creados(self, obj):
        cursos = ', '.join([str(curso) for curso in obj.cursos_creados()])
        return cursos if cursos else '-'
    
    cursos_creados.short_description = 'Cursos Creados'

admin.site.register(Profesor, ProfesorAdmin)