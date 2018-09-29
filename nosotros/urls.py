from django.conf.urls import url

from . import views
from .views import NosotrosPageView
urlpatterns = [
    #url(r'^', views.nosotros, name='nosotros'),
    url(r'^', NosotrosPageView.as_view(), name='nosotros'),
]