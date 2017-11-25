from django.conf.urls import url, include
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='datail'),
    url(r'^create/$', views.create),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.delete),
    url(r'^create/$', views.create),
]
