from django.conf.urls import patterns, url
from open import views

urlpatterns = patterns('',
		url(r'^index/$', views.index, name='index'),
		url(r'^home/$', views.home, name='home'),
		url(r'^profile/$', views.profile, name='profile'),
		url(r'^about/$', views.about, name='about'),
		)
