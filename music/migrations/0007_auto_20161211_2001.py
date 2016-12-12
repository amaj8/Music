# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20161211_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(upload_to='uploads/%Y/%M/%d'),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default=None, upload_to='uploads/%Y/%M/%d'),
        ),
    ]