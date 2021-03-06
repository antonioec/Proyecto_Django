# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-01 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import viviendas.models


class Migration(migrations.Migration):

    dependencies = [
        ('viviendas', '0014_remove_vivienda_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda',
            name='imagen',
            field=models.ImageField(upload_to=viviendas.models.custom_upload_to_vivienda, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='vivienda_gallery',
            name='imagen_gallery',
            field=models.ImageField(upload_to=viviendas.models.custom_upload_to_gallery, verbose_name='Imagen de galer\xeda'),
        ),
    ]
