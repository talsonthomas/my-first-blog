from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.login),
 	url(r'^logout/$', views.logout),
	url(r'^home/$', views.home, name='home'),
]
