# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-07 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import viviendas.models


class Migration(migrations.Migration):

    dependencies = [
        ('viviendas', '0024_auto_20181005_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vivienda',
            name='superficie',
        ),
        migrations.RemoveField(
            model_name='vivienda_gallery',
            name='titulo',
        ),
        migrations.AddField(
            model_name='vivienda',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, verbose_name='Direcci\xf3n'),
        ),
        migrations.AddField(
            model_name='vivienda',
            name='superficie_construida',
            field=models.FloatField(blank=True, default=0, verbose_name='Superficie Construida'),
        ),
        migrations.AddField(
            model_name='vivienda',
            name='superficie_parcela',
            field=models.FloatField(blank=True, default=0, verbose_name='Superficie Parcela'),
        ),
        migrations.AddField(
            model_name='vivienda',
            name='superficie_util',
            field=models.FloatField(blank=True, default=0, verbose_name='Superficie Util'),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='antiguedad',
            field=models.IntegerField(blank=True, verbose_name='Antig\xfcedad'),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=viviendas.models.custom_upload_to_vivienda, verbose_name='Imagen de Portada'),
        ),
    ]