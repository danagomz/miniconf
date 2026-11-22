"""Modelos de la app articulos: artículos enviados y sus revisiones."""

from django.conf import settings
from django.db import models


class Articulo(models.Model):
    """Artículo enviado por un autor a la conferencia."""

    class Estado(models.TextChoices):
        """Estados posibles de un artículo durante la revisión."""

        ENVIADO = "enviado", "Enviado"
        EN_REVISION = "en revision", "En revisión"
        ACEPTADO = "aceptado", "Aceptado"
        RECHAZADO = "rechazado", "Rechazado"

    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articulos",
    )
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.ENVIADO,
    )
    palabras_clave = models.CharField(max_length=200, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Ordenamiento y nombres legibles del modelo."""

        ordering = ["-fecha"]
        verbose_name = "artículo"
        verbose_name_plural = "artículos"

    def __str__(self) -> str:
        """Devuelve el título del artículo."""
        return self.titulo


class Revision(models.Model):
    """Calificación que un revisor le da a un artículo."""

    articulo = models.ForeignKey(
        Articulo,
        on_delete=models.CASCADE,
        related_name="revisiones",
    )
    nota = models.IntegerField()
    comentario = models.TextField(blank=True)

    class Meta:
        """Nombres legibles del modelo."""

        verbose_name = "revisión"
        verbose_name_plural = "revisiones"

    def __str__(self) -> str:
        """Devuelve el artículo y la nota de la revisión."""
        return f"{self.articulo} - nota {self.nota}"
