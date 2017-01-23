from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Company(models.Model):
    name = models.CharField("Company Name", max_length=250)
    ticker = models.CharField("Ticker", max_length=10, unique=True)
    exchange = models.CharField("Stock Exchange", max_length=100, blank=True, null=True)
    market_cap = models.BigIntegerField("Market Cap", blank=True, null=True)
    beta = models.FloatField("Beta", blank=True, null=True)
    PE_ratio = models.FloatField("P/E Ratio", blank=True, null=True)
    EPS = models.FloatField("Earnings Per Share", blank=True, null=True)
    Price_To_Sales = models.FloatField("Price To Sales", blank=True, null=True)
    Price_To_Book = models.FloatField("Price to Book", blank=True, null=True)
    EV_To_Rev = models.FloatField("EV to Revenue", blank=True, null=True)
    EV_To_EBITDA = models.FloatField("EV to EBITDA", blank=True, null=True)
    sector = models.CharField(max_length=250, blank=True, null=True)
    industry = models.CharField(max_length=250, blank=True, null=True)
    employee_count = models.IntegerField(blank=True, null=True)

    def __str__ (self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Companies"

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = PhoneNumberField(blank=True, null=True)
    receive_text = models.BooleanField(blank=True)
    receive_email = models.BooleanField(blank=True)

    def __str__ (self):
        return str(self.user.username)

    class Meta:
        verbose_name_plural = 'User Profiles (Additional User Info)'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class UserCompanies(models.Model):
    user = models.OneToOneField(User)
    tracked_company = models.ManyToManyField(Company)

    def __str__ (self):
        return str(self.user.username)

    class Meta:
        ordering = ['tracked_company__name']
        verbose_name_plural = 'User Tracked Companies'
