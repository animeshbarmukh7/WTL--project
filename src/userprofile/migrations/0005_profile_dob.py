# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_profile_m_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
