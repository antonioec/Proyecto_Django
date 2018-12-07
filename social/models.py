# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Social(models.Model):
    id = models.SlugField(verbose_name="Social_key", primary_key=True)
    nombre = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    publicacion = models.DateField(verbose_name="Publicación", auto_now_add=True)
    actualizacion = models.DateField(verbose_name="Actualización", auto_now=True)

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"

    def __str__(self):
        return self.nombre