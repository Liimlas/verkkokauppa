# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
