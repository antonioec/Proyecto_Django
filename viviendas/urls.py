
from django.conf.urls import url

from .views import ViviendasListView, ViviendaDetailView
urlpatterns = [
    url(r'^$', ViviendasListView.as_view(), name='viviendas'),
    url(r'^(?P<pk>[0-9]+)/(?P<slug>[\w-]+)', ViviendaDetailView.as_view(), name='vivienda'),
]
