from django.conf.urls import patterns, include, url
from django.conf import settings
<<<<<<< HEAD
=======

>>>>>>> a037bfd5f2de04bce05e8c344e66f321379e1413
from django.contrib import admin
from filebrowser import sites

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('content.urls', namespace="content")),
)

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )