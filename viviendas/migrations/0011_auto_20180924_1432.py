# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-24 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viviendas', '0010_auto_20180924_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda_gallery',
            name='imagen_gallery',
            field=models.FileField(upload_to='projects/gallery/', verbose_name='Imagen de galer\xeda'),
        ),
    ]
