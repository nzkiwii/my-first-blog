from home.models import *
from .forms import UpdateCompaniesForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import HttpResponse

def user_profile(request, username):
    #BUG: Can't sort datatable by intword (market cap column)
    updated = False
    currently_tracked_text = []
    user = request.user
    currently_tracked = []

    user_company_model = UserCompanies.objects.get_or_create(user=user)

    if user_company_model[0].tracked_company.all().count() > 0:
        for c in user_company_model[0].tracked_company.all():
            currently_tracked.append(c)
    else:
        currently_tracked = []
    for company in currently_tracked:
        currently_tracked_text.append(str(company.id))
    form = UpdateCompaniesForm(instance=user_company_model[0])
    #all_companies = Company.objects.all()
    if request.method == 'POST':
        form = UpdateCompaniesForm(request.POST, instance=user_company_model[0])
        if form.is_valid():
            form.save()
            updated = True
            messages.success(request, 'Your tracked companies have been updated!')
            return HttpResponseRedirect(reverse('user_profile', kwargs={'username':user.username}))

        else:
            messages.error(request, 'Shit\'s not working correctly.')
            return HttpResponseRedirect(reverse('user_profile', kwargs={'username':user.username}))
    else:

        return render(request, 'user_profile/user_profile.html', {'user': user,
                                                                  #'all_companies': all_companies,
                                                                  'user_company_model': user_company_model,
                                                                  'currently_tracked': currently_tracked,
                                                                  'currently_tracked_text': currently_tracked_text,
                                                                  'form': form,
                                                                  'updated': updated,
                                                                 })

def get_companies(request):
    all_companies = Company.objects.all()
    json = serializers.serialize('json', all_companies)
    with open('json.txt', 'w') as f:
        f.write(json)

    return HttpResponse(json, content_type='application/json')
