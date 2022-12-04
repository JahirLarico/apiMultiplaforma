from rest_framework import serializers
from .models import Recetas


class RecetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recetas
        fields = ['id','imagen', 'nombre', 'descripcion', 'tipo', 'pasos', 'favoritos']