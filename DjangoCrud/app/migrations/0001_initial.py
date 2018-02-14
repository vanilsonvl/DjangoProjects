# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-27 21:09
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2000)])),
                ('value', models.FloatField()),
                ('register_date', models.DateTimeField(default=datetime.datetime(2017, 12, 27, 21, 8, 59, 383933))),
            ],
        ),
    ]
