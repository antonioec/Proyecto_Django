# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-12 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import logotipo.models


class Migration(migrations.Migration):

    dependencies = [
        ('logotipo', '0005_auto_20181004_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='logotipo',
            name='imagen_mobile',
            field=models.ImageField(null=True, upload_to=logotipo.models.custom_upload_to_mobile, verbose_name='Logotipo peque\xf1o'),
        ),
    ]
