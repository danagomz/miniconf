"""Rutas principales del proyecto MiniConf."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("articulos.urls")),
]
