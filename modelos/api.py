from .models import Modelo
from rest_framework import viewsets, permissions
from .serializer import ModeloSerializer

class ModelosViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ModeloSerializer