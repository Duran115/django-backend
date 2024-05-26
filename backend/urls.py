from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('usuario/', include('usuario.urls')),
    path('estudiante/', include('estudiante.urls')),
    path('profesor/', include('profesor.urls')),
    path('curso/', include('curso.urls')),
    path('matricula/', include('matricula.urls')),
    path('horario/', include('horario.urls')),
    path('calificacion/', include('calificacion.urls')),
]