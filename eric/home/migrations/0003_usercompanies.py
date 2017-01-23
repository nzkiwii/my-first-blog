# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 03:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20161106_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_list', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Tracked Companies',
            },
        ),
    ]
