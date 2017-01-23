from django.contrib import admin
from home.models import Company, UserCompanies

class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['ticker','name']

# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(UserCompanies)
