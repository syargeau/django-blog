# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]