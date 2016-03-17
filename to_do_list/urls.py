from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'to_do.views.home', name='home'),
	url(r'^register/','to_do.views.signup'),
	#url(r'^weather/','to_do.views.weather'),
	url(r'^login/','to_do.views.login'),
	url(r'^logout/','to_do.views.logout'),
	url(r'^admin/', include(admin.site.urls)),
]
