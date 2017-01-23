# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Region Name')),
                ('ticker', models.CharField(max_length=5, unique=True, verbose_name='Ticker')),
                ('exchange', models.CharField(blank=True, max_length=100, null=True, verbose_name='Stock Exchange')),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
    ]