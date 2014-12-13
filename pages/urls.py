from django.conf.urls import patterns, url
from pages import views

urlpatterns = patterns('',
	# url(r'^(?P<url>.*/)$', views.page_index),
	url(r'^(?P<url>.*)/$', views.page, name="page"),
)