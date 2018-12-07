# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Social
# Register your models here.

class SocialAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Clientes").exists():
            return ('publicacion', 'actualizacion', 'id',)
        else:
            return ('publicacion', 'actualizacion')

    list_display = ('nombre', 'link')

admin.site.register(Social, SocialAdmin)