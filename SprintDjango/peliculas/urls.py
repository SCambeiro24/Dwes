from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PeliculaViewSet, GeneroViewSet

# Definimos el router y registramos los ViewSets
router = DefaultRouter()
router.register(r'peliculas', PeliculaViewSet, basename='pelicula')
router.register(r'generos', GeneroViewSet, basename='genero')

# Las URLs finales se generan automáticamente
urlpatterns = [
    path('', include(router.urls)),
]