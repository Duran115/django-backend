from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'profesor', 'get_estudiantes_matriculados']
    
    def get_estudiantes_matriculados(self, obj):
        estudiantes = ', '.join([str(estudiante) for estudiante in obj.estudiantes_matriculados()])
        return estudiantes if estudiantes else '-'
    
    get_estudiantes_matriculados.short_description = 'Estudiantes Matriculados'

admin.site.register(Curso, CursoAdmin)
