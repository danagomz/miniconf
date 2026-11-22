"""Registro de los modelos de articulos en el panel de administración."""

from django.contrib import admin

from .models import Articulo, Revision


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    """Configuración del admin para los artículos."""

    list_display = ["titulo", "autor", "estado", "fecha"]
    list_filter = ["estado"]
    search_fields = ["titulo", "palabras_clave"]


@admin.register(Revision)
class RevisionAdmin(admin.ModelAdmin):
    """Configuración del admin para las revisiones."""

    list_display = ["articulo", "nota"]
