"""Configuración de la app articulos."""

from django.apps import AppConfig


class ArticulosConfig(AppConfig):
    """Registra la app articulos en Django."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "articulos"
