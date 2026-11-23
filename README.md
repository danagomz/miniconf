# MiniConf

API en Django REST Framework para la Demo-exposición 9. Empezó escrita mal a propósito (rama `codigo-sucio`) y cada integrante limpió su parte.

## Correr el proyecto

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac / Linux

pip install -r requirements.txt
copy .env.example .env         # Windows  (Mac / Linux: cp .env.example .env)
```

Abre `.env` y cambia `DJANGO_SECRET_KEY` por cualquier texto largo. Después:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Admin (para crear artículos y revisiones): http://127.0.0.1:8000/admin/
- API: http://127.0.0.1:8000/api/articulos/

## Tests

```bash
python manage.py test
```

Deben salir **OK (6 tests)**.

## Contador de errores

```bash
ruff check . --isolated --preview --select E,W,F,I,N,D,ANN,DJ --ignore D203,D213 --extend-exclude migrations --statistics
```

| Etapa | Tag | Errores |
| --- | --- | --- |
| Código sucio | `v0-sucio` | 256 |
| PEP 8 | `v1-pep8` | 198 |
| Código legible | `v2-legible` | 155 |
| Estándares de Django | `v3-django` | 49 |
| Automatización | `v4-automatizado` | 0 |

## Revisión automática

La configuración de Ruff está en `pyproject.toml`. Para revisar y formatear todo el proyecto:

```bash
ruff check .
ruff format .
```

Para que Ruff revise cada commit antes de guardarlo (una sola vez por computador):

```bash
pip install pre-commit
pre-commit install
```

En GitHub, el workflow `.github/workflows/calidad.yml` corre Ruff y los tests en cada push y pull request.
