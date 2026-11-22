from rest_framework import serializers

from .models import articulo
from .utils import formatear_titulo


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = articulo
        fields = ['id', 'Titulo', 'resumen', 'palabrasClave', 'estado']
        read_only_fields = ['estado']

    def validate_Titulo(self, valor):
        if valor is None or valor.strip() == '':
            raise serializers.ValidationError('El titulo no puede estar vacio')
        return formatear_titulo(valor)
