# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Politica
from django.views.generic.detail import DetailView
# Create your views here.

class PoliticasDetailView(DetailView):
    model = Politica
