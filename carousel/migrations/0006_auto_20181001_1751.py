# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-01 15:51
from __future__ import unicode_literals

import carousel.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0005_auto_20181001_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='imagen',
            field=models.ImageField(upload_to=carousel.models.custom_upload_to, verbose_name='Imagen'),
        ),
    ]
