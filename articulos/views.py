from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import ArticuloSerializer
from .services import *

@api_view(['GET','POST'])
def articulos(request):
    if request.method=='GET':
        datos=[]
        for x in articulo.objects.all():
            revs=revision.objects.filter(art=x)
            total=0
            for r in revs:
                total=total+r.nota
            if len(revs)>0:
                prom=total/len(revs)
            else:
                prom=0
            if prom>=4:
                x.estado='aceptado'
                x.save()
            datos.append({'id':x.id,'Titulo':x.Titulo,'autor':x.a.username,'estado':x.estado,'promedio':prom,'url':'/api/articulos/'+str(x.id)+'/'})
        return Response(datos)
    s=ArticuloSerializer(data=request.data)
    if s.is_valid():
        s.save(a=request.user)
        return Response(s.data,status=201)
    return Response(s.errors,status=400)

@api_view(['GET'])
def detalle(request,id):
    try:
        x=articulo.objects.get(id=id)
    except:
        return Response({'error':'no existe'},status=404)
    return Response({'id':x.id,'Titulo':x.Titulo,'resumen':x.resumen,'autor':x.a.username,'estado':x.estado})
