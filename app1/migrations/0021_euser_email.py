# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-23 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_remove_euser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='euser',
            name='email',
            field=models.EmailField(blank=True, default=0, max_length=254),
        ),
    ]