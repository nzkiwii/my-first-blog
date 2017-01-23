from django.db import models
from django.contrib.auth.models import User
from home.models import UserCompanies
from django import forms
from django.utils.translation import ugettext_lazy as _

class UpdateCompaniesForm(forms.ModelForm):

     class Meta:
        labels = {
            'user': _(''),
            'tracked_company': _(''),
        }
        model = UserCompanies
        fields = '__all__'
