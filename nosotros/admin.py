# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Nosotros

# Register your models here.

class NosotrosAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Clientes").exists():
            return ('titulo',)
        else:
            return ()

    list_display = ('titulo', 'contenido')
    ordering = ('id',)

admin.site.register(Nosotros, NosotrosAdmin)