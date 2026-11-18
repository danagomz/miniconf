# MiniConf

API en Django REST Framework escrita mal a propósito para la Demo-exposición 9. Cada uno limpia su parte.

## Correr el proyecto

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac / Linux
 
pip install -r requirements.txt
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

Deben salir **OK (6 tests)** antes y después de tu refactor.

## Contador de errores

```bash
ruff check . --isolated --preview --select E,W,F,I,N,D,ANN,DJ --ignore D203,D213 --extend-exclude migrations --statistics
```

En `codigo-sucio` da **Found 256 errors**.

## Para trabajar

- No toques la rama `codigo-sucio`.
- Crea tu rama desde `main`, cambia solo tus archivos y fusiona en tu fecha (ver el doc del grupo).