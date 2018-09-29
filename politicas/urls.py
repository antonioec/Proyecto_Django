
from django.conf.urls import url
from .views import PoliticasDetailView

from . import views
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/(?P<slug>[\w-]+)', PoliticasDetailView.as_view(), name='politicas'),
]