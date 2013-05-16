from django.conf.urls import patterns, include, url
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbc.views.home', name='home'),
    # url(r'^bbc/', include('bbc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$','django.contrib.auth.views.login',name='home'),
    url(r'^login/$','django.contrib.auth.views.login',name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/login'},name='logout'),
    url(r'^test/$','infant.views.test',name='test'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
