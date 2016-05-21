from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from articles.models import Article
from django.views.generic import ListView

urlpatterns = patterns('histoire',
    # Examples:
    #url(r'^$', ListView.as_view(model=Article,
    #                context_object_name="last_articles",
    #                template_name="base.html")),
    url(r'^$', 'views.home', name='home'),
    url(r'^articles/', include('articles.urls')),
    url(r'^network/', include('network.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
