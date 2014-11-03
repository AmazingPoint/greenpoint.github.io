from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
	url(r'accounts/login/$', auth_views.login, {'template_name': 'osb/login.html'}),
	url(r'accounts/logout/$', auth_views.logout, {'template_name': 'osb/logout.html'}),
    url(r'^osb/', include('osb.urls')),
)
