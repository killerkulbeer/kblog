from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.posts_list, name="list"),
    url(r'^create/$', views.posts_create, name="create"),
    url(r'^about/$', views.about, name="about"),
    url(r'^(?P<slug>[\w-]+)/$', views.posts_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.posts_update, name="edit"),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.posts_delete, name="delete"),
]
