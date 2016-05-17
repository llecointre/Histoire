from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('articles',
    url(r'^read/(?P<id>\d+)', 'views.read'),
)
