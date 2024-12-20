from django.db import models
from django.core.exceptions import ValidationError

class Modelo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.FloatField()
    fecha_fabricacion = models.DateField()
    imagen_principal = models.URLField(null=True, blank=True)  # Solo un campo para URL de imagen
    descripcion_principal = models.TextField()

    # Usamos JSONField para almacenar las características como una lista de diccionarios
    caracteristicas = models.JSONField(default=list, blank=True)

    def clean(self):
        # Validar que si se proporciona una imagen, sea una URL válida
        if self.imagen_principal:
            if not self.imagen_principal.startswith("http"):
                raise ValidationError("La URL de la imagen debe comenzar con 'http'.")
            # Opcionalmente, puedes agregar más validaciones para asegurar que la URL sea una imagen válida (como extensión .jpg, .png, etc.)
            if not any(self.imagen_principal.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif']):
                raise ValidationError("La URL debe apuntar a una imagen válida (por ejemplo, .jpg, .jpeg, .png).")

        super().clean()

    def __str__(self):
        return self.modelo
