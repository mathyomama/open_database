from django.conf.urls import patterns, url
from open import views

urlpatterns = patterns('',
		url(r'^$', views.home, name='home'),
		url(r'^index/$', views.index, name='index'),
		url(r'^jobs/$', views.job_listing, name='jobs'),
		url(r'^add_company/$', views.add_company, name='add_company'),
		url(r'^profile/$', views.profile, name='profile'),
		url(r'^about/$', views.about, name='about'),
		)
