from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assets_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^cascade', TemplateView.as_view(template_name='resources/cascade.html')),
    url(r'^purecss', TemplateView.as_view(template_name='compress/purecss.html')),
    url(r'^bootstrap', TemplateView.as_view(template_name='less/bootstrap.html')),
    url(r'^foundation', TemplateView.as_view(template_name='sass/foundation.html')),

    url(r'^admin/', include(admin.site.urls)),
)
