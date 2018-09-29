# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Carousel
# Register your models here.

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'titulo', 'descripcion', 'link', 'imagen')

admin.site.register(Carousel, CarouselAdmin)