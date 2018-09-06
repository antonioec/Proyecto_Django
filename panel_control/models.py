# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.timezone import now


# Create your models here.

@python_2_unicode_compatible
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
    imagen = models.ImageField(verbose_name="Imagen", upload_to="projects")
    descripcion = models.TextField(verbose_name="Descripción")
    antiguedad = models.DateField(max_length=255, verbose_name="Antigüedad")
    publicacion = models.DateField(verbose_name="Publicación", default=now)

    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    altitud = models.CharField(max_length=255, verbose_name="Altitud")
    latitud = models.CharField(max_length=255, verbose_name="Latitud")
    eficiencia = models.CharField(max_length=255, verbose_name="Eficiencia")

    class Meta:
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"
        ordering = ["-publicacion"]

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField()
    publicacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-publicacion"]

    def __str__(self):
        return self.nombre

class Carousel(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="projects")
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")

    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousel"

    def __str__(self):
        return self.titulo

class Social(models.Model):
    id = models.SlugField(verbose_name="Social_key", primary_key=True, unique=True)
    nombre = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"

    def __str__(self):
        return self.nombre

class Destacado(models.Model):
    id = models.AutoField(primary_key=True)
    identificador = models.IntegerField(verbose_name="Identificador de Vivienda destacada", default=0)
    titulo = models.CharField(max_length=255, verbose_name="Título")

    class Meta:
        verbose_name = "Destacado"
        verbose_name_plural = "Destacados"

    def __str__(self):
        return self.titulo


