# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20180304_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='ageRestriction',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='infotext',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
