from django.contrib import admin
from .models import Matricula

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'curso', 'fecha_matricula']
    
    def estudiante(self, obj):
        return obj.estudiante
    
    def curso(self, obj):
        return obj.curso
    
    def fecha_matricula(self, obj):
        return obj.fecha_matricula

admin.site.register(Matricula, MatriculaAdmin)