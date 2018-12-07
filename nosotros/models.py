# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

@python_2_unicode_compatible
class Nosotros(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    publicacion = models.DateField(verbose_name="Publicación", auto_now_add=True)
    actualizacion = models.DateField(verbose_name="Actualización", auto_now=True)

    class Meta:
        verbose_name = "Nosotros"
        verbose_name_plural = "Nosotros"

    def __str__(self):
        return self.titulo