from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['correo', 'is_admin']
    list_filter = ['is_admin']

admin.site.register(Usuario, UsuarioAdmin)