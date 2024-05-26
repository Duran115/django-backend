from django.contrib import admin
from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['correo', 'nombre', 'apellidos', 'universidad', 'carrera', 'ciclo', 'codigo', 'cursos_matriculados']
    
    def cursos_matriculados(self, obj):
        cursos = ', '.join([str(curso) for curso in obj.cursos_matriculados()])
        return cursos if cursos else '-'
    
    cursos_matriculados.short_description = 'Cursos Matriculados'

admin.site.register(Estudiante, EstudianteAdmin)