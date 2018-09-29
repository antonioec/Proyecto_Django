# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from models import Nosotros

# Create your views here.

#def nosotros(request):
#    nosotros = get_object_or_404(Nosotros)
#    return render(request, "web/nosotros.html", {'nosotros':nosotros})

class NosotrosPageView(TemplateView):

    template_name = "web/nosotros.html"

    def get(self, request, *args, **kwargs):
        nosotros = get_object_or_404(Nosotros)
        return render(request, self.template_name, {'nosotros': nosotros})