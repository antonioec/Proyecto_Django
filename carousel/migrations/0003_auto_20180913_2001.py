# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0002_auto_20180913_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='descripcion',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='titulo',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='T\xedtulo'),
        ),
    ]