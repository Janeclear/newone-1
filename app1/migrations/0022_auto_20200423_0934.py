# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-23 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_euser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='euser',
            name='aspect',
        ),
        migrations.RemoveField(
            model_name='euser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='euser',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='euser',
            name='usernumber',
        ),
    ]
