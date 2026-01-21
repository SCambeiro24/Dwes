from rest_framework.viewsets import ModelViewSet
from .models import Pelicula, Genero
from .serializers import PeliculaSerializer, GeneroSerializer

# ModelViewSet incluye: list, retrieve, create, update y destroy
class PeliculaViewSet(ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer