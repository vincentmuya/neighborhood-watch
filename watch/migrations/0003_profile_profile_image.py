# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_remove_profile_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
