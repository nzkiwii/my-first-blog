# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-26 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20161224_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='market_cap',
        ),
    ]