from .models import revision

def calc(a,l):
    # calcula
    x=0
    tmp=0
    i=0
    for n in l:
        x=x+n
        i=i+1 # suma 1 a i
    if i==0:
        return 0
    tmp=x/i
    return round(tmp,a)

def procesar(articulo):
    # validar
    t=articulo.Titulo
    if t==None or len(t)>200:
        return False
    if len(articulo.resumen)<20:
        return False
    # calcular promedio
    l=[]
    for r in revision.objects.filter(art=articulo):
        if r.nota>5 or r.nota<1:
            continue
        l.append(r.nota)
    p=calc(2,l)
    # cambiar estado
    if p>=4:
        articulo.estado='aceptado'
    elif p>=3:
        articulo.estado='en revision'
    elif len(l)>0:
        articulo.estado='rechazado'
    articulo.save()
    #if p>=4.5:
    #    enviar_correo(articulo.a.email)
    #    print('aceptado con honores')
    return True
