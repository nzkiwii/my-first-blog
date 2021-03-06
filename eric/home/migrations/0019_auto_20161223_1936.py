# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20161220_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='EPS',
            field=models.FloatField(blank=True, null=True, verbose_name='Earnings Per Share'),
        ),
        migrations.AddField(
            model_name='company',
            name='EV_To_EBITDA',
            field=models.FloatField(blank=True, null=True, verbose_name='EV to EBITDA'),
        ),
        migrations.AddField(
            model_name='company',
            name='EV_To_Rev',
            field=models.FloatField(blank=True, null=True, verbose_name='EV to Revenue'),
        ),
        migrations.AddField(
            model_name='company',
            name='PE_ratio',
            field=models.FloatField(blank=True, null=True, verbose_name='P/E Ratio'),
        ),
        migrations.AddField(
            model_name='company',
            name='Price_To_Book',
            field=models.FloatField(blank=True, null=True, verbose_name='Price to Book'),
        ),
        migrations.AddField(
            model_name='company',
            name='Price_To_Sales',
            field=models.FloatField(blank=True, null=True, verbose_name='Price To Sales'),
        ),
        migrations.AddField(
            model_name='company',
            name='beta',
            field=models.FloatField(blank=True, null=True, verbose_name='Beta'),
        ),
        migrations.AddField(
            model_name='company',
            name='market_cap',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Market Cap'),
        ),
    ]
