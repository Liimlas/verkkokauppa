# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20180218_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='user_pictures'),
        ),
    ]