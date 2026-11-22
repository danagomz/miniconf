"""Rutas de la API de articulos."""

from django.urls import path

from . import views

app_name = "articulos"

urlpatterns = [
    path("articulos/", views.lista_articulos, name="lista"),
    path("articulos/<int:pk>/", views.detalle_articulo, name="detalle"),
]
