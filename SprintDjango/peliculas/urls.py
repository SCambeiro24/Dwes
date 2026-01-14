from django.urls import path
from .views import PeliculaListAPIView, PeliculaDetailAPIView

urlpatterns = [
    path('api/peliculas/', PeliculaListAPIView.as_view()),       # Para lista y POST
    path('api/peliculas/<int:pk>/', PeliculaDetailAPIView.as_view()), # Para el detalle
]