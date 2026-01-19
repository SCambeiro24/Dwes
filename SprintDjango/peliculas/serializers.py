from rest_framework import serializers
from .models import Pelicula, Genero

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'sinopsis', 'fecha_estreno', 'duracion_minutos', 'precio_alquiler', 'genero']
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def validate_precio_alquiler(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio de alquiler no puede ser negativo")
        return value