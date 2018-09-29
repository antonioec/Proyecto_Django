
from django.conf.urls import url

from . import views
from .views import HomePageView
urlpatterns = [
    #url(r'^$', views.home, name='home'),
    url(r'^$', HomePageView.as_view(), name='home'),
]