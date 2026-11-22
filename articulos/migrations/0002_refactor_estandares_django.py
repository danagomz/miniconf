# Migración escrita a mano para el refactor de estándares de Django.
# Django no detecta solo que "a" pasó a ser "autor" (porque también cambió
# su related_name), así que los renombres se declaran explícitamente para
# conservar los datos en vez de borrar y crear columnas nuevas.

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def vacios_a_texto(apps, schema_editor):
    """Cambia los NULL de palabras_clave por texto vacío antes de quitar null=True."""
    Articulo = apps.get_model("articulos", "Articulo")
    Articulo.objects.filter(palabras_clave__isnull=True).update(palabras_clave="")


class Migration(migrations.Migration):

    dependencies = [
        ("articulos", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # 1. Renombrar campos (conservan sus datos).
        migrations.RenameField(
            model_name="articulo", old_name="Titulo", new_name="titulo"
        ),
        migrations.RenameField(
            model_name="articulo", old_name="a", new_name="autor"
        ),
        migrations.RenameField(
            model_name="articulo",
            old_name="palabrasClave",
            new_name="palabras_clave",
        ),
        migrations.RenameField(
            model_name="revision", old_name="art", new_name="articulo"
        ),
        # 2. Pasar los NULL a "" y luego quitar null=True.
        migrations.RunPython(vacios_a_texto, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="articulo",
            name="palabras_clave",
            field=models.CharField(blank=True, max_length=200),
        ),
        # 3. Estado con choices.
        migrations.AlterField(
            model_name="articulo",
            name="estado",
            field=models.CharField(
                choices=[
                    ("enviado", "Enviado"),
                    ("en revision", "En revisión"),
                    ("aceptado", "Aceptado"),
                    ("rechazado", "Rechazado"),
                ],
                default="enviado",
                max_length=20,
            ),
        ),
        # 4. related_name en las relaciones.
        migrations.AlterField(
            model_name="articulo",
            name="autor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="articulos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="revision",
            name="articulo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="revisiones",
                to="articulos.articulo",
            ),
        ),
        # 5. Opciones de Meta (orden y nombres legibles).
        migrations.AlterModelOptions(
            name="articulo",
            options={
                "ordering": ["-fecha"],
                "verbose_name": "artículo",
                "verbose_name_plural": "artículos",
            },
        ),
        migrations.AlterModelOptions(
            name="revision",
            options={"verbose_name": "revisión", "verbose_name_plural": "revisiones"},
        ),
    ]