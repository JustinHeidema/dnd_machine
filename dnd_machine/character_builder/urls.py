from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'character_builder'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<pk>[a-zA-Z]+)/$', views.race_api),
]


# (?P<pk>[a-zA-Z]+)