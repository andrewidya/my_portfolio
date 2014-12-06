from django.conf.urls import patterns, url
from content import views


urlpatterns = patterns('',
	url(r'^(?P<url>[a-z/]*)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<post_id>\d+)/(?P<permalink>[-\w]+)/$', views.get_post, name="post"),
	url(r'^$', views.index, name="index"),
)

urlpatterns += patterns('',
	url(r'(?P<url>[a-z/]*[^0-9])/$', views.archive, name="archive"),
)