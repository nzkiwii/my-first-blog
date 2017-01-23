from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^company-filings/$', views.company_filings, name='company_filings'),
    url(r'^get-company-filings/$', views.get_company_filings, name='get_company_filings'),
]
