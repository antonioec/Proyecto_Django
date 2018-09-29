# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

@python_2_unicode_compatible
class Carousel(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="projects")
    nombre = models.CharField(max_length=255, verbose_name="Nombre", default='')
    titulo = models.CharField(max_length=255, verbose_name="Título", blank=True, null=True)
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")

    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousel"

    def __str__(self):
        return self.nombre