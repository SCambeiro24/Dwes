from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # Importante para los códigos de error
from .models import Pelicula

class PeliculaListAPIView(APIView):
    def get(self, request):
        peliculas = Pelicula.objects.all()
        data = []
        for peli in peliculas:
            data.append({
                'id': peli.id,
                'titulo': peli.titulo,
                'duracion': peli.duracion_minutos
            })
        return Response(data)


    def post(self, request):
        nueva_peli = Pelicula.objects.create(
            titulo=request.data.get('titulo'),
            sinopsis=request.data.get('sinopsis'),
            fecha_estreno=request.data.get('fecha_estreno'),
            duracion_minutos=request.data.get('duracion_minutos'),
            precio_alquiler=request.data.get('precio_alquiler')
        )
        return Response({"mensaje": "Película creada con éxito"}, status=status.HTTP_201_CREATED)


class PeliculaDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            p = Pelicula.objects.get(pk=pk)
            return Response({
                'id': p.id,
                'titulo': p.titulo,
                'sinopsis': p.sinopsis
            })
        except Pelicula.DoesNotExist:
            return Response({"error": "Película no encontrada"}, status=status.HTTP_404_NOT_FOUND)