# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-14 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180214_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
