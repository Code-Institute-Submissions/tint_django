# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-03 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0036_transcriptdetails_purchased_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcriptdetails',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
