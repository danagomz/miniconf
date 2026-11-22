"""Lógica de negocio de MiniConf: validación, promedios y estado de artículos."""

from .models import articulo, revision

DECIMALES_PROMEDIO = 2
NOTA_MINIMA = 1
NOTA_MAXIMA = 5
LONGITUD_MAXIMA_TITULO = 200
LONGITUD_MINIMA_RESUMEN = 20

ESTADO_ACEPTADO = "aceptado"
ESTADO_EN_REVISION = "en revision"
ESTADO_RECHAZADO = "rechazado"

PROMEDIO_MINIMO_ACEPTACION = 4
PROMEDIO_MINIMO_REVISION = 3


def calcular_promedio_calificaciones(
    calificaciones: list[int],
    decimales: int = DECIMALES_PROMEDIO,
) -> float:
    """Calcula el promedio de una lista de calificaciones.

    Args:
        calificaciones: Lista de notas que se van a promediar.
        decimales: Cantidad de decimales del resultado.

    Returns:
        El promedio redondeado o 0 si la lista está vacía.

    """
    if not calificaciones:
        return 0.0

    promedio = sum(calificaciones) / len(calificaciones)
    return round(promedio, decimales)


def validar_articulo(articulo_actual: articulo) -> bool:
    """Valida el título y el resumen de un artículo.

    Args:
        articulo_actual: Artículo que se va a validar.

    Returns:
        True si cumple las condiciones de validación, False en caso contrario.

    """
    titulo = articulo_actual.Titulo
    resumen = articulo_actual.resumen

    if titulo is None or len(titulo) > LONGITUD_MAXIMA_TITULO:
        return False

    if len(resumen) < LONGITUD_MINIMA_RESUMEN:
        return False

    return True


def obtener_calificaciones_validas(
    articulo_actual: articulo,
) -> list[int]:
    """Obtiene las calificaciones válidas de las revisiones de un artículo.

    Args:
        articulo_actual: Artículo del que se consultarán las revisiones.

    Returns:
        Lista de notas entre la nota mínima y la máxima permitida.

    """
    return list(
        revision.objects.filter(
            art=articulo_actual,
            nota__gte=NOTA_MINIMA,
            nota__lte=NOTA_MAXIMA,
        ).values_list("nota", flat=True)
    )


def actualizar_estado_articulo(
    articulo_actual: articulo,
    promedio: float,
    cantidad_calificaciones: int,
) -> None:
    """Actualiza el estado del artículo según el promedio de sus calificaciones."""
    if promedio >= PROMEDIO_MINIMO_ACEPTACION:
        articulo_actual.estado = ESTADO_ACEPTADO
    elif promedio >= PROMEDIO_MINIMO_REVISION:
        articulo_actual.estado = ESTADO_EN_REVISION
    elif cantidad_calificaciones > 0:
        articulo_actual.estado = ESTADO_RECHAZADO


def procesar_articulo(articulo_actual: articulo) -> bool:
    """Valida un artículo, calcula su promedio y actualiza su estado.

    Args:
        articulo_actual: Artículo que se va a procesar.

    Returns:
        True si el artículo fue procesado, False si no es válido.

    """
    if not validar_articulo(articulo_actual):
        return False

    calificaciones = obtener_calificaciones_validas(articulo_actual)
    promedio = calcular_promedio_calificaciones(calificaciones)

    actualizar_estado_articulo(
        articulo_actual,
        promedio,
        len(calificaciones),
    )

    articulo_actual.save()
    return True
