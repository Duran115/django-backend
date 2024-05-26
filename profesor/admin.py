from django.contrib import admin
from .models import Profesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['correo', 'nombre', 'apellidos', 'profesion', 'centro_laboral', 'cursos_creados', 'puntuacion_promedio']
    
    def cursos_creados(self, obj):
        cursos = ', '.join([str(curso) for curso in obj.cursos_creados()])
        return cursos if cursos else '-'
    
    def puntuacion_promedio(self, obj):
        return obj.mostrar_puntuacion()
    
    cursos_creados.short_description = 'Cursos Creados'
    puntuacion_promedio.short_description = 'Puntuación'

admin.site.register(Profesor, ProfesorAdmin)