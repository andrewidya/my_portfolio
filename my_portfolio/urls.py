from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/filebrowser/', include(site.get_urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('content.urls', namespace="content")),
)

urlpatterns += patterns('',
    url(r'^', include('pages.urls', namespace="pages")),
)

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )