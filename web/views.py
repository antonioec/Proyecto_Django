# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView

#def home(request):
#   return render(request, "web/home.html")

class HomePageView(TemplateView):
    template_name = "web/home.html"
