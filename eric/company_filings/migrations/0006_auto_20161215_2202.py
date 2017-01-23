# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_filings', '0005_remove_securityacquired_transaction_code_v'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securityacquired',
            name='shares_owned_following_transaction',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='securityacquired',
            name='transaction_shares',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
