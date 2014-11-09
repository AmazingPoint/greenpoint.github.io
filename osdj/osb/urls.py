from django.conf.urls import patterns, url

from osb import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	url(r'^chat/$', views.chat, name="chat"),
	url(r'^getFromuser/$', views.getFromuser, name="getFromuser"),
	url(r'^checkMessageNumber/$', views.checkMessageNumber, name="checkMessageNumber"),
	url(r'^sendMessage/(?P<userid>\d+)/$', views.sendMessage, name="sendMessage"),
	url(r'^getMessage/(?P<fuserid>\d+)/$', views.getMessage, name="getMessage"),
	url(r'^setMessageReaded/(?P<messageid>\d+)/$', views.setMessageReaded, name="setMessageReaded"),
)
