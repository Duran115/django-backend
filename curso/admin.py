from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'profesor', 'mostrar_estudiantes_matriculados']

    def mostrar_estudiantes_matriculados(self, obj):
        estudiantes = ', '.join([str(estudiante) for estudiante in obj.estudiantes_matriculados])
        return estudiantes if estudiantes else '-'

    mostrar_estudiantes_matriculados.short_description = 'Estudiantes Matriculados'

admin.site.register(Curso, CursoAdmin)
