def formatear_titulo(titulo):
    nombre_limpio = titulo.strip()
    if nombre_limpio is None:
        return ''
    return nombre_limpio[0].upper() + nombre_limpio[1:]


def formatear_fecha(fecha, formato_largo=False):
    if formato_largo:
        return fecha.strftime('%d/%m/%Y a las %H:%M')
    return fecha.strftime('%d/%m/%Y')


def es_vacio(texto):
    return texto is None or len(texto.strip()) == 0


def generar_cita(titulo, nombre_autor, fecha):
    return (
        f"{nombre_autor} ({fecha.year}).{titulo}. "
        "Memorias de la Conferencia Cientifica MiniConf, "
        "Universidad del valle, Cali, Colombia."
    )
