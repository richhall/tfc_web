# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0018_auto_20170328_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclejourney',
            name='departure_time',
            field=models.TimeField(),
        ),
    ]