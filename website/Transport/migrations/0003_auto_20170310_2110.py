# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-10 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transport', '0002_auto_20170223_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='Driver_latitude',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Driver_longitude',
            field=models.FloatField(default=None, null=True),
        ),
    ]
