# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_files', models.FileField(upload_to='client_files/audio_files')),
                ('video_files', models.FileField(upload_to='client_files/audio_files')),
            ],
        ),
    ]
