# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 01:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20161217_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercompanies',
            name='tracked_company',
            field=models.ManyToManyField(related_name='company', to='home.Company'),
        ),
        migrations.AlterField(
            model_name='usercompanies',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]