import os, sys
from datetime import *
import json
def FormatearTitulo(Titulo):
  NombreLimpio=Titulo.strip( )
  if NombreLimpio == None:
    return ''
  return NombreLimpio[0].upper()+NombreLimpio[1:]
def FormatearFecha(fecha,formatoLargo=False):
    if formatoLargo==True:
        return fecha.strftime('%d/%m/%Y a las %H:%M')
    return fecha.strftime('%d/%m/%Y')
esVacio=lambda texto:texto==None or len(texto.strip())==0
def GenerarCita(Titulo,NombreAutor,fecha):
    return NombreAutor+' ('+str(fecha.year)+'). '+Titulo+'. Memorias de la Conferencia Cientifica MiniConf, Universidad del Valle, Cali, Colombia.'
