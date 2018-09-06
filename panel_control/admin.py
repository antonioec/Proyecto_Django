# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Vivienda, Comentarios, Carousel, Social, Destacado

# Register your models here.

# Mostrar campos de solo lectura en el panel de administrador
class ViviendaAdmin(admin.ModelAdmin):
    readonly_fields = ('publicacion',)
    list_display = ('titulo', 'tipo', 'ubicacion', 'publicacion', 'id', 'imagen')
    search_fields = ('titulo', 'tipo', 'publicacion')
    ordering = ('publicacion',)
    list_filter = ('tipo', 'ubicacion')

class ComentariosAdmin(admin.ModelAdmin):
    readonly_fields = ('publicacion',)
    list_display = ('nombre', 'email', 'publicacion')
    search_fields = ('nombre', 'email', 'publicacion')
    ordering = ('publicacion',)

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'link', 'imagen')

class SocialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'link')

class DestacadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'identificador')

admin.site.register(Vivienda, ViviendaAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Destacado, DestacadoAdmin)