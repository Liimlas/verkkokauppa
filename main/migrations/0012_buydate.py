# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180224_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Game')),
            ],
        ),
    ]
