# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 20:21
from __future__ import unicode_literals
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LWDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_class', models.CharField(choices=[('A', 'A'), ('C', 'C')], max_length=1)),
                ('counters_size', models.IntegerField(choices=[(2, 2), (4, 4)])),
                ('dev_addr', models.CharField(max_length=32)),
                ('nwkskey', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
