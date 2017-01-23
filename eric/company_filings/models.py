from django.db import models
from home.models import *

# Create your models here.

class CompanyFiling(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    report_owner_name = models.CharField(max_length=250, blank=True, null=True)
    ticker = models.CharField(max_length=250, blank=True, null=True)
    is_officer = models.NullBooleanField(blank=True, null=True)
    is_director = models.NullBooleanField(blank=True, null=True)
    is_ten_percent_owner = models.NullBooleanField(blank=True, null=True)
    officer_title = models.CharField(max_length=250, blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    filing_date = models.DateField(blank=True, null=True)

    def __str__ (self):
        return str(self.company)

    class Meta:
        verbose_name_plural = "Company Filings"

class SecurityAcquired(models.Model):
    filing = models.ForeignKey(CompanyFiling, on_delete=models.CASCADE)
    url = models.CharField(max_length=250, blank=True, null=True)
    security_title = models.CharField(max_length=250, blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    transaction_form_type = models.CharField(max_length=250, blank=True, null=True)
    transaction_code  = models.CharField(max_length=250, blank=True, null=True)
    transaction_shares = models.FloatField(blank=True, null=True)
    transaction_price_per_share = models.FloatField(blank=True, null=True)
    transaction_acquired_disposed_code = models.CharField(max_length=250, blank=True, null=True)
    shares_owned_following_transaction = models.FloatField(blank=True, null=True)
    direct_or_indirect_ownership = models.CharField(max_length=250, blank=True, null=True)


    class Meta:
        verbose_name_plural = "Securities Acquired"
