# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0023_auto_20170520_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfiles',
            name='details',
        ),
    ]