# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-18 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0015_remove_neighborhood_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Neighborhood',
        ),
        migrations.AddField(
            model_name='profile',
            name='Neighborhood',
            field=models.ManyToManyField(to='watch.Neighborhood'),
        ),
    ]
