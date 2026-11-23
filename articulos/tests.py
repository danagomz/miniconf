"""Pruebas de MiniConf: modelos, servicios y endpoints de la API."""

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Articulo, Revision
from .services import calcular_promedio_calificaciones, procesar_articulo

URL_ARTICULOS = "/api/articulos/"
TIPO_JSON = "application/json"


class PruebasMiniConf(TestCase):
    """Pruebas que deben pasar antes y después de cada refactor."""

    def setUp(self) -> None:
        """Crea un autor y un artículo de base para cada prueba."""
        self.autor = User.objects.create_user(
            "autor1", "autor1@correo.com", "clave12345"
        )
        self.art = Articulo.objects.create(
            titulo="Redes neuronales en agricultura",
            resumen="Un resumen suficientemente largo para la prueba.",
            autor=self.autor,
        )

    def test_crear_articulo(self) -> None:
        """Un artículo nuevo queda guardado y con estado 'enviado'."""
        self.assertEqual(Articulo.objects.count(), 1)
        self.assertEqual(self.art.estado, "enviado")

    def test_promedio(self) -> None:
        """El promedio se calcula bien y una lista vacía da 0."""
        self.assertEqual(calcular_promedio_calificaciones([4, 5, 3]), 4.0)
        self.assertEqual(calcular_promedio_calificaciones([]), 0)

    def test_procesar_acepta_con_buen_promedio(self) -> None:
        """Un artículo con promedio de 4.5 queda aceptado."""
        Revision.objects.create(articulo=self.art, nota=5)
        Revision.objects.create(articulo=self.art, nota=4)
        procesar_articulo(self.art)
        self.assertEqual(self.art.estado, "aceptado")

    def test_lista_responde_200(self) -> None:
        """La lista de artículos responde 200 y muestra el título."""
        Revision.objects.create(articulo=self.art, nota=3)
        respuesta = self.client.get(URL_ARTICULOS)
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Redes neuronales en agricultura")

    def test_crear_por_api(self) -> None:
        """Un usuario autenticado puede crear un artículo por la API."""
        self.client.force_login(self.autor)
        datos = {
            "titulo": "vision por computador",
            "resumen": "Un resumen de prueba para la API.",
        }
        respuesta = self.client.post(URL_ARTICULOS, datos, content_type=TIPO_JSON)
        self.assertEqual(respuesta.status_code, 201)
        self.assertEqual(Articulo.objects.count(), 2)

    def test_api_rechaza_titulo_vacio(self) -> None:
        """La API responde 400 si el título viene vacío."""
        self.client.force_login(self.autor)
        datos = {"titulo": "", "resumen": "Un resumen cualquiera"}
        respuesta = self.client.post(URL_ARTICULOS, datos, content_type=TIPO_JSON)
        self.assertEqual(respuesta.status_code, 400)
