from django.db import models
from django.contrib.auth.models import *

class articulo(models.Model):
    class Meta:
        verbose_name_plural='articulos'
    Titulo=models.CharField(max_length=200)
    resumen=models.TextField()
    a=models.ForeignKey(User,on_delete=models.CASCADE)
    estado=models.CharField(max_length=20,default='enviado')
    palabrasClave=models.CharField(max_length=200,null=True,blank=True)
    fecha=models.DateTimeField(auto_now_add=True)

class revision(models.Model):
    art=models.ForeignKey(articulo,on_delete=models.CASCADE)
    nota=models.IntegerField()
    comentario=models.TextField(blank=True)
