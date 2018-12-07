# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

from django.db import models

# Create your models here.

def custom_upload_to(instance, filename):
    try:
        old_instance = instance.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return "projects/carousel/" + filename
    except:
        return "projects/carousel/" + filename

@python_2_unicode_compatible
class Carousel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="Nombre", default='')
    imagen = models.ImageField(verbose_name="Imagen (Máx. 10MB)", upload_to=custom_upload_to, blank=True)
    titulo = models.CharField(max_length=255, verbose_name="Título", blank=True, null=True)
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    activado = models.BooleanField(default=True, verbose_name="Activada")
    publicacion = models.DateField(verbose_name="Publicación", auto_now_add=True)
    actualizacion = models.DateField(verbose_name="Actualización", auto_now=True)

    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousel"
        ordering = ["-publicacion"]

    def __str__(self):
        return self.nombre