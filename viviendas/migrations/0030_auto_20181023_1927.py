# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import viviendas.models


class Migration(migrations.Migration):

    dependencies = [
        ('viviendas', '0029_auto_20181023_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=viviendas.models.custom_upload_to_vivienda, verbose_name='Imagen de Portada (M\xe1x. 10MB)'),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='planos',
            field=models.FileField(blank=True, default='', upload_to=viviendas.models.custom_upload_to_planos, verbose_name='Planos de vivienda (PDF) (M\xe1x. 10MB)'),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='video',
            field=models.FileField(blank=True, default='', upload_to=viviendas.models.custom_upload_to_video, verbose_name='Video (M\xe1x. 10MB)'),
        ),
        migrations.AlterField(
            model_name='vivienda_gallery',
            name='imagen_gallery',
            field=models.ImageField(upload_to=viviendas.models.custom_upload_to_gallery, verbose_name='Imagen de galer\xeda (M\xe1x. 10MB)'),
        ),
    ]
