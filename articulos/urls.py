from django.urls import path
from . import views

urlpatterns = [
    path('articulos/',views.articulos),
    path('articulos/<int:id>/',views.detalle),
]
