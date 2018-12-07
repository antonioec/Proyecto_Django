# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import os

# Create your models here.

def custom_upload_to_gallery(instance, filename):
    try:
        old_instance = instance.objects.get(pk=instance.pk)
        old_instance.imagen_gallery.delete()
        return "projects/gallery/" + filename
    except:
        return "projects/gallery/" + filename

def custom_upload_to_vivienda(instance, filename):
    try:
        old_instance = instance.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return "projects/viviendas_image/" + filename
    except:
        return "projects/viviendas_image/" + filename

def custom_upload_to_planos(instance, filename):
    try:
        old_instance = instance.objects.get(pk=instance.pk)
        old_instance.planos.delete()
        return "projects/planos/" + filename
    except:
        return "projects/planos/" + filename

def custom_upload_to_video(instance, filename):
    try:
        old_instance = instance.objects.get(pk=instance.pk)
        old_instance.video.delete()
        return "projects/video/" + filename
    except:
        return "projects/video/" + filename

@python_2_unicode_compatible
class Vivienda_gallery(models.Model):
    id = models.AutoField(primary_key=True)
    imagen_gallery = models.ImageField(verbose_name="Imagen de galería (Máx. 10MB)", upload_to=custom_upload_to_gallery)
    publicacion = models.DateField(verbose_name="Publicación", auto_now_add=True)
    actualizacion = models.DateField(verbose_name="Actualización", auto_now=True)

    class Meta:
        verbose_name = "Galería de propiedad"
        verbose_name_plural = "Galerías de propiedades"
        ordering = ["-publicacion"]

    def __str__(self):
        return os.path.basename(self.imagen_gallery.name)

@python_2_unicode_compatible
class Vivienda(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identificador")
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    operacion = models.CharField(max_length=255, verbose_name="Operación", blank=True, null=True)
    precio = models.IntegerField(verbose_name="Precio", blank=True, null=True)
    ciudad = models.CharField(max_length=255, verbose_name="Ciudad", blank=True, null=True)
    direccion = models.CharField(max_length=255, verbose_name="Dirección", blank=True, null=True)
    tipo = models.CharField(max_length=255, verbose_name="Tipo", blank=True, null=True)
    dormitorios = models.IntegerField(verbose_name="Dormitorios", blank=True, null=True)
    banos = models.IntegerField(verbose_name="Baños", blank=True, null=True)
    aseos = models.IntegerField(verbose_name="Aseos", blank=True, null=True)

    superficie_construida = models.FloatField(verbose_name="Superficie Construida", blank=True, default=0)
    superficie_util = models.FloatField(verbose_name="Superficie Util", blank=True, default=0)
    superficie_parcela = models.FloatField(verbose_name="Superficie Parcela", blank=True, default=0)

    imagen = models.ImageField(verbose_name="Imagen de Portada (Máx. 10MB)", upload_to=custom_upload_to_vivienda, blank=True, null=True)
    galeria = models.ManyToManyField(Vivienda_gallery, verbose_name="Imágenes de galería", blank=True)
    planos = models.FileField(verbose_name="Planos de propiedad (PDF) (Máx. 10MB)", upload_to=custom_upload_to_planos, default="", blank=True)
    video = models.FileField(verbose_name="Video (Máx. 10MB)", upload_to=custom_upload_to_video, default="", blank=True)
    activado = models.BooleanField(default=True, verbose_name="Activada")
    destacado = models.BooleanField(default=False, verbose_name="Propiedad destacada")
    antiguedad = models.IntegerField(verbose_name="Antigüedad", blank=True, null=True)
    altitud = models.CharField(max_length=255, verbose_name="Altitud", blank=True, null=True)
    latitud = models.CharField(max_length=255, verbose_name="Latitud", blank=True, null=True)
    eficiencia = models.CharField(max_length=255, verbose_name="Eficiencia", blank=True, null=True)
    publicacion = models.DateField(verbose_name="Publicación", auto_now_add=True)
    actualizacion = models.DateField(verbose_name="Actualización", auto_now=True)

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ["-publicacion"]

    def __str__(self):
        return self.titulo
