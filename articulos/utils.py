"""Funciones de apoyo para dar formato a textos y fechas de MiniConf."""

from datetime import datetime


def formatear_titulo(titulo: str) -> str:
    """Quita espacios sobrantes y pone en mayúscula la primera letra del título."""
    nombre_limpio = titulo.strip()
    if nombre_limpio is None:
        return ""
    return nombre_limpio[0].upper() + nombre_limpio[1:]


def formatear_fecha(fecha: datetime, formato_largo: bool = False) -> str:
    """Devuelve la fecha como texto, con o sin la hora."""
    if formato_largo:
        return fecha.strftime("%d/%m/%Y a las %H:%M")
    return fecha.strftime("%d/%m/%Y")


def es_vacio(texto: str | None) -> bool:
    """Indica si el texto es None o solo tiene espacios."""
    return texto is None or len(texto.strip()) == 0


def generar_cita(titulo: str, nombre_autor: str, fecha: datetime) -> str:
    """Arma la cita bibliográfica de un artículo de la conferencia."""
    return (
        f"{nombre_autor} ({fecha.year}).{titulo}. "
        "Memorias de la Conferencia Cientifica MiniConf, "
        "Universidad del valle, Cali, Colombia."
    )
