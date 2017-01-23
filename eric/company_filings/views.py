from home.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from company_filings.models import *
from home.models import UserCompanies
from django.core import serializers

# Create your views here.
'''Shows the most recent filings and defaults to the users tracked companies.
Outputs the most recent filings in a datatable.'''
def company_filings(request):
    user_company_list = []
    all_filings = CompanyFiling.objects.all()
    json = serializers.serialize('json', all_filings)
    #all_filings = SecurityAcquired.objects.all()

    return render(request, 'company_filings/company_filings.html', {'all_filings': all_filings,
                                                                     'user_company_list': user_company_list,})

def get_company_filings(request):
    user_company_list = []
    #user = request.user
    #user_companies = UserCompanies.objects.get(user=user)

    all_filings = CompanyFiling.objects.all()
    json = serializers.serialize('json', all_filings)

    return HttpResponse(json, content_type='application/json')
