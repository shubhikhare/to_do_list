from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'to_do.views.home', name='home'),
	url(r'^register/','to_do.views.signup'),
	url(r'^delete/','to_do.views.delete'),
	url(r'^edit/','to_do.views.edit'),
	url(r'^addtask/','to_do.views.addtask'),
	url(r'^login/','to_do.views.login'),
	url(r'^logout/','to_do.views.logout'),
	url(r'^display/','to_do.views.display'),
	url(r'^admin/', include(admin.site.urls)),
]
