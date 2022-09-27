from django.urls import path
from .views import home, generales, programacion, videojuegos, tecnologias, tutoriales, detallePost

urlpatterns = [
    path('',home, name = 'index'),
    path('generales/', generales, name = 'generales'),    
    path('programacion/', programacion, name = 'programacion'),
    path('videojuegos/', videojuegos, name = 'videojuegos'),
    path('tecnologias/', tecnologias, name = 'tecnologias'),
    path('tutoriales/', tutoriales, name = 'tutoriales'),
    path('<slug:slug>/', detallePost, name = 'detalle_post'),
]