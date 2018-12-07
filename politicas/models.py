# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Politica(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    contenido = models.TextField(verbose_name="Contenido", blank=True, null=True)
    activado = models.BooleanField(default=True, verbose_name="Activada")
    publicacion = models.DateField(verbose_name="Publicación", auto_now_add=True)
    actualizacion = models.DateField(verbose_name="Actualización", auto_now=True)

    class Meta:
        verbose_name = "Politica"
        verbose_name_plural = "Politicas"
        ordering = ["-id"]

    def __str__(self):
        return self.nombre