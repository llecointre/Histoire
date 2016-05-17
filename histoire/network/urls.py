from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
from django.views.generic import DetailView
from network.models import Profil

urlpatterns = patterns('network',
    url(r'^login/', 'views.log_in', name='login'),
    url(r'^logout/', 'views.log_out', name='logout'),
    url(r'^$', 'views.profil', name='profil'),
    #url(r'^login$', auth_views.login, {'template_name': 'login.html'}),
    #url(r'^logout$', auth_views.logout, {'next_page': '/'}),
)
