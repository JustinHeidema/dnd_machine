from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'character_builder'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'test/', views.test, name='test'),
    url(r'api/races/(?P<pk>[a-zA-Z]+)/$', views.race_api),
    url(r'api/classes/(?P<pk>[a-zA-Z]+)/$', views.class_api),
]
