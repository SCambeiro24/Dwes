from rest_framework import serializers
from .models import Pelicula, Genero

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):

    genero_nombre = serializers.ReadOnlyField(source='genero.nombre')

    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'sinopsis', 'fecha_estreno', 'duracion_minutos', 'precio_alquiler', 'genero_nombre']