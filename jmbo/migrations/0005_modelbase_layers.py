# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-19 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0002_auto_20161219_1041'),
        ('jmbo', '0004_photosize_name_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelbase',
            name='layers',
            field=models.ManyToManyField(blank=True, help_text='Makes item eligible to be published on selected layers.', null=True, to='layers.Layer'),
        ),
    ]
