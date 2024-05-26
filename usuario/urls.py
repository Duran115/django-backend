from django.urls import path
from . import views

urlpatterns = [
    path('est/', views.estudiante),
    path('pro/', views.profesor),
]