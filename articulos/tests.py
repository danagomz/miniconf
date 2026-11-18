from django.contrib.auth.models import User
from django.test import TestCase

from .models import articulo, revision
from .services import calc, procesar

# OJO: si en tu refactor renombras un modelo, un campo o una funcion,
# actualiza tambien los nombres aqui. Lo que NO puede cambiar es el
# resultado esperado de cada prueba.


class PruebasMiniConf(TestCase):
    def setUp(self):
        self.autor = User.objects.create_user("autor1", "autor1@correo.com", "clave12345")
        self.art = articulo.objects.create(
            Titulo="Redes neuronales en agricultura",
            resumen="Un resumen suficientemente largo para la prueba.",
            a=self.autor,
        )

    def test_crear_articulo(self):
        self.assertEqual(articulo.objects.count(), 1)
        self.assertEqual(self.art.estado, "enviado")

    def test_promedio(self):
        self.assertEqual(calc(2, [4, 5, 3]), 4.0)
        self.assertEqual(calc(2, []), 0)

    def test_procesar_acepta_con_buen_promedio(self):
        revision.objects.create(art=self.art, nota=5)
        revision.objects.create(art=self.art, nota=4)
        procesar(self.art)
        self.assertEqual(self.art.estado, "aceptado")

    def test_lista_responde_200(self):
        revision.objects.create(art=self.art, nota=3)
        respuesta = self.client.get("/api/articulos/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Redes neuronales en agricultura")

    def test_crear_por_api(self):
        self.client.force_login(self.autor)
        datos = {"Titulo": "vision por computador", "resumen": "Un resumen de prueba para la API."}
        respuesta = self.client.post("/api/articulos/", datos, content_type="application/json")
        self.assertEqual(respuesta.status_code, 201)
        self.assertEqual(articulo.objects.count(), 2)

    def test_api_rechaza_titulo_vacio(self):
        self.client.force_login(self.autor)
        datos = {"Titulo": "", "resumen": "Un resumen cualquiera"}
        respuesta = self.client.post("/api/articulos/", datos, content_type="application/json")
        self.assertEqual(respuesta.status_code, 400)
