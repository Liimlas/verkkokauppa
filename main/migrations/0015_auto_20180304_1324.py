# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sold',
            name='copies',
        ),
        migrations.AddField(
            model_name='boughtgame',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='sold',
        ),
    ]
