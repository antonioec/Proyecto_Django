# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

# Create your models here.

@python_2_unicode_compatible
class Vivienda_gallery(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255, verbose_name="Título galería de vivienda", default="")
    imagen_gallery = models.ImageField(verbose_name="Imagen de galería", upload_to="projects/gallery/")
    publicacion = models.DateField(verbose_name="Publicación", default=now)

    class Meta:
        verbose_name = "Galería de vivienda"
        verbose_name_plural = "Galerías de viviendas"
        ordering = ["-publicacion"]

    def __str__(self):
        return self.titulo

class Vivienda(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    titulo = models.CharField(max_length=255, verbose_name="Título")
    operacion = models.CharField(max_length=255, verbose_name="Operación")
    dormitorios = models.IntegerField(verbose_name="Dormitorios")
    precio = models.IntegerField(verbose_name="Precio")
    superficie = models.IntegerField(verbose_name="Superficie")
    ubicacion = models.CharField(max_length=255, verbose_name="Ubicación")
    tipo = models.CharField(max_length=255, verbose_name="Tipo")
    banos = models.IntegerField(verbose_name="Baños")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="projects/viviendas_image/")
    galeria = models.ManyToManyField(Vivienda_gallery, verbose_name="Imágenes de galería")
    descripcion = models.TextField(verbose_name="Descripción")
    destacado = models.BooleanField(default=False, verbose_name="Vivienda destacada")
    antiguedad = models.DateField(max_length=255, verbose_name="Antigüedad")
    publicacion = models.DateField(verbose_name="Publicación", default=now)

    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    altitud = models.CharField(max_length=255, verbose_name="Altitud", default='None')
    latitud = models.CharField(max_length=255, verbose_name="Latitud", default='None')
    eficiencia = models.CharField(max_length=255, verbose_name="Eficiencia", default='None')

    class Meta:
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"
        ordering = ["-publicacion"]

    def __str__(self):
        return self.titulo
