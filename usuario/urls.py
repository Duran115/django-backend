from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('signup/', views.signup, name='signup'),
    path('signup/estudiante/', views.signup_estudiante, name='signup_estudiante'),
    path('signup/profesor/', views.signup_profesor, name='signup_profesor'),
    path('signin/', views.signin, name='signin'),
    path('api/v1/', include(router.urls)),
]
