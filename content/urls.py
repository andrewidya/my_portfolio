from django.conf.urls import patterns, url
from content import views


urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	url(r'^home/', views.index, name="index"),
	url(r'^post/(?P<year>\d{4})/(?P<month>\d{2})/(?P<post_id>\d+)/(?P<permalink>[-\w]+)/$', views.get_post, name="post"),
	url(r'about/', views.about, name="about"),
	url(r'^category/$', views.get_category, name="category"),
)

urlpatterns += patterns('',
	url(r'^post/$', views.get_post_list, name="post_list"),
)