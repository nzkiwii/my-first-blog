from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user-profile/(?P<username>[-\w.]+)/$', views.user_profile, name='user_profile'),
    url(r'^get-companies/$', views.get_companies, name='get_companies'),
]
