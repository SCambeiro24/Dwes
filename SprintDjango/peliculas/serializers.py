from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Pelicula, Genero, Perfil, Reseña


# 1. Relación 1:1
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografía', 'fecha_nacimiento']


# 2. Relación 1:N
class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nombre', 'descripcion']


# 3. Relación N:M
class ReseñaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseña
        fields = ['id', 'usuario', 'pelicula', 'puntuacion', 'comentario', 'created_at']


# 4. El Recurso Principal
class PeliculaSerializer(serializers.ModelSerializer):
    genero_detalle = GeneroSerializer(source='genero', read_only=True)
    genero = serializers.PrimaryKeyRelatedField(
        queryset=Genero.objects.all(),
        write_only=True
    )
    reseñas = ReseñaSerializer(many=True, read_only=True)

    class Meta:
        model = Pelicula
        fields = [
            'id', 'titulo', 'sinopsis', 'fecha_estreno', 'duracion_minutos',
            'precio_alquiler', 'genero', 'genero_detalle', 'reseñas'
        ]

    def validate_precio_alquiler(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo")
        return value