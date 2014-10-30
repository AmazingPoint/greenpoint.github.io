from django.conf.urls import patterns, url

from osb import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
)
