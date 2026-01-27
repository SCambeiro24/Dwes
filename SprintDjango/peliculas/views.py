from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .models import Pelicula, Genero, Reseña, Perfil
from .serializers import ( PeliculaSerializer, GeneroSerializer, ReseñaSerializer,  PerfilSerializer, UserSerializer)

# ModelViewSet incluye automáticamente: list, retrieve, create, update y destroy

class PeliculaViewSet(ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class ReseñaViewSet(ModelViewSet):
    queryset = Reseña.objects.all()
    serializer_class = ReseñaSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PerfilViewSet(ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer