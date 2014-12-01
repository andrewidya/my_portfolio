from django.conf.urls import patterns, url
from content import views


urlpatterns = patterns('',
	#url(r'^(?P<url>[a-z/]*)$', views.archive), # added from pages app
	url(r'^(?P<url>[a-z/]*)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<post_id>\d+)/(?P<permalink>\w+)/$', views.single_post, name="single_post_show"),
)

urlpatterns += patterns('',
    (r'^(?P<url>.*/)$', views.archive),
)
