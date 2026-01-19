from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pelicula
from .serializers import PeliculaSerializer

class PeliculaListAPIView(APIView):
    def get(self, request):
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PeliculaDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            peli = Pelicula.objects.get(pk=pk)
            serializer = PeliculaSerializer(peli)
            return Response(serializer.data)
        except Pelicula.DoesNotExist:
            return Response({"error": "No encontrada"}, status=status.HTTP_404_NOT_FOUND)