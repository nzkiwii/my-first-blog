# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20161220_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercompanies',
            name='tracked_company',
            field=models.ManyToManyField(to='home.Company'),
        ),
    ]
