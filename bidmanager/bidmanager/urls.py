from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'bids.views.home', name='home'),
                       url(r'^about$', 'bids.views.about', name='about'),
                       url(r'^contact$', 'bids.views.contact', name='contact'),
                       url(r'^how-to$', 'bids.views.howto', name='howto'),
                       # url(r'^bidmanager/', include('bidmanager.foo.urls')),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^profile/login/$', 'profiles.views.login_user'),
                       url(r'^admin/', include(admin.site.urls)),
                       )


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    )
