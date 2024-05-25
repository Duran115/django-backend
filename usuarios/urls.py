from django.urls import path
from . import views

urlpatterns = [
    path('estudiante/', views.estudiante),
    path('profesor/', views.profesor),
]
