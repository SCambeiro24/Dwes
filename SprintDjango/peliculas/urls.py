from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PeliculaViewSet, GeneroViewSet, ReseñaViewSet, UserViewSet, PerfilViewSet)

# Creamos el router y registramos todos los recursos del Diagrama ER
router = DefaultRouter()
router.register(r'peliculas', PeliculaViewSet, basename='pelicula')
router.register(r'generos', GeneroViewSet, basename='genero')
router.register(r'resenas', ReseñaViewSet, basename='resena')
router.register(r'usuarios', UserViewSet, basename='usuario')
router.register(r'perfiles', PerfilViewSet, basename='perfil')

urlpatterns = [
    path('', include(router.urls)),
]