# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-03 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viviendas', '0017_vivienda_activado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda',
            name='superficie',
            field=models.FloatField(verbose_name='Superficie'),
        ),
    ]
