from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Importamos todos los ViewSets que creamos en views.py
from .views import (
    PeliculaViewSet,
    GeneroViewSet,
    ReseñaViewSet,
    UserViewSet,
    PerfilViewSet
)

# Configuramos el router para generar las URLs automáticamente
router = DefaultRouter()
router.register(r'peliculas', PeliculaViewSet, basename='pelicula')
router.register(r'generos', GeneroViewSet, basename='genero')
# Usamos 'resenas' sin ñ para evitar fallos de compatibilidad
router.register(r'resenas', ReseñaViewSet, basename='resena')
router.register(r'usuarios', UserViewSet, basename='usuario')
router.register(r'perfiles', PerfilViewSet, basename='perfil')

urlpatterns = [
    # Incluimos todas las rutas registradas en el router
    path('', include(router.urls)),
]