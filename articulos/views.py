"""Vistas de la API de articulos."""

from django.urls import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Articulo
from .serializers import ArticuloSerializer
from .services import (
    calcular_promedio_calificaciones,
    obtener_calificaciones_validas,
)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def lista_articulos(request: Request) -> Response:
    """Lista los artículos con su promedio o crea uno nuevo."""
    if request.method == "POST":
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(autor=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    datos = []
    for articulo in Articulo.objects.select_related("autor"):
        calificaciones = obtener_calificaciones_validas(articulo)
        datos.append(
            {
                "id": articulo.pk,
                "titulo": articulo.titulo,
                "autor": articulo.autor.username,
                "estado": articulo.estado,
                "promedio": calcular_promedio_calificaciones(calificaciones),
                "url": reverse("articulos:detalle", args=[articulo.pk]),
            }
        )
    return Response(datos)


@api_view(["GET"])
def detalle_articulo(request: Request, pk: int) -> Response:
    """Devuelve el detalle de un artículo o un error 404 si no existe."""
    try:
        articulo = Articulo.objects.select_related("autor").get(pk=pk)
    except Articulo.DoesNotExist:
        return Response({"error": "no existe"}, status=404)

    return Response(
        {
            "id": articulo.pk,
            "titulo": articulo.titulo,
            "resumen": articulo.resumen,
            "autor": articulo.autor.username,
            "estado": articulo.estado,
        }
    )
