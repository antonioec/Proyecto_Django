# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-14 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viviendas', '0025_auto_20181007_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda',
            name='altitud',
            field=models.CharField(blank=True, max_length=255, verbose_name='Altitud'),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='eficiencia',
            field=models.CharField(blank=True, max_length=255, verbose_name='Eficiencia'),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='latitud',
            field=models.CharField(blank=True, max_length=255, verbose_name='Latitud'),
        ),
    ]
