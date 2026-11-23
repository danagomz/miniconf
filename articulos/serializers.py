"""Serializers de la API de articulos."""

from rest_framework import serializers

from .models import Articulo
from .utils import formatear_titulo


class ArticuloSerializer(serializers.ModelSerializer):
    """Convierte artículos a JSON y valida los datos que llegan a la API."""

    class Meta:
        """Campos del artículo que expone la API."""

        model = Articulo
        fields = ["id", "titulo", "resumen", "palabras_clave", "estado"]
        read_only_fields = ["estado"]

    def validate_titulo(self, valor: str) -> str:
        """Rechaza títulos vacíos y les da formato a los válidos."""
        if valor is None or valor.strip() == "":
            raise serializers.ValidationError("El titulo no puede estar vacio")
        return formatear_titulo(valor)
