# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0027_transcriptdetails_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcriptdetails',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
