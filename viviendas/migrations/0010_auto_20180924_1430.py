# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-24 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viviendas', '0009_auto_20180924_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda_gallery',
            name='imagen_gallery',
            field=models.ImageField(upload_to='http://a06e01c97.appspot.com/media/projects/gallery/', verbose_name='Imagen de galer\xeda'),
        ),
    ]
