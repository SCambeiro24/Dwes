from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint


# 1. TABLA: Perfil (Relación 1:1 con User)
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    es_premium = models.BooleanField(default=False)
    biografia = models.TextField(blank=True, verbose_name="Biografía")

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"Perfil de {self.usuario.username}"


# 2. TABLA: Genero (Relación 1:N con Pelicula)
class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# 3. TABLA: Pelicula (Recurso Principal)
class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    fecha_estreno = models.DateField()
    duracion_minutos = models.IntegerField(help_text="Duración en minutos")
    precio_alquiler = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Requisito Decimal

    # Relación 1:N
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, related_name="peliculas")

    # Relación N:M explícita con modelo intermedio
    espectadores = models.ManyToManyField(User, through='Reseña', related_name="peliculas_vistas")

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ['-fecha_estreno']

    def __str__(self):
        return self.titulo


# 4. TABLA: Reseña (Modelo Intermedio N:M entre User y Pelicula)
class Reseña(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    # Campos extra de la relación (Atributos de la N:M)
    puntuacion = models.IntegerField(help_text="Escala de 1 a 5")
    comentario = models.TextField()

    # Campos de Auditoría (Requisito)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        # Restricción de Unicidad (Requisito): Un usuario solo puede reseñar cada película una vez
        constraints = [
            UniqueConstraint(fields=['usuario', 'pelicula'], name='unique_usuario_pelicula_resena')
        ]

    def __str__(self):
        return f"Reseña de {self.usuario.username} sobre {self.pelicula.titulo}"