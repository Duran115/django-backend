from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'profesor', 'get_estudiantes_matriculados', 'get_horarios']
    
    def get_estudiantes_matriculados(self, obj):
        estudiantes = ', '.join([str(estudiante) for estudiante in obj.estudiantes_matriculados()])
        return estudiantes if estudiantes else '-'
    
    def get_horarios(self, obj):
        horarios = ', '.join([str(horario) for horario in obj.mostrar_horarios()])
        return horarios if horarios else '-'
    
    get_estudiantes_matriculados.short_description = 'Estudiantes Matriculados'
    get_horarios.short_description = 'Horarios'

admin.site.register(Curso, CursoAdmin)
