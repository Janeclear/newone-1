# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-03-25 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20200214_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='email',
            field=models.EmailField(blank=True, default=0, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(blank=True, default=0, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='password',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='test',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], default='男', max_length=32),
        ),
    ]
