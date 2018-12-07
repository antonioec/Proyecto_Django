# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Carousel
# Register your models here.

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activado', 'titulo', 'descripcion', 'link', 'imagen')
    search_fields = ('activado', 'titulo', 'publicacion')
    ordering = ('-publicacion',)
    list_filter = ('nombre', 'activado',)
    readonly_fields = ('actualizacion', )

admin.site.register(Carousel, CarouselAdmin)