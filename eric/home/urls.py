from django.conf.urls import url, include
from django.contrib.auth.views import *
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_form/$', views.register_form, name='register_form'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^how/$', views.how, name='how'),
    url(r'^performance/$', views.performance, name='performance'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")),
]
