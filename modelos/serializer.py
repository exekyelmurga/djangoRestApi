from rest_framework import serializers
from .models import Modelo

class ModeloSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Modelo
        fields = ('id', 'modelo', 'marca', 'categoria', 'precio', 'fecha_fabricacion'
                  , 'imagen_principal', 'descripcion_principal', 'caracteristicas')