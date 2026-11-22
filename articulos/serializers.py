from rest_framework import serializers

from .models import Articulo
from .utils import formatear_titulo


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id', 'titulo', 'resumen', 'palabras_clave', 'estado']
        read_only_fields = ['estado']

    def validate_titulo(self, valor):
        if valor is None or valor.strip() == '':
            raise serializers.ValidationError('El titulo no puede estar vacio')
        return formatear_titulo(valor)
