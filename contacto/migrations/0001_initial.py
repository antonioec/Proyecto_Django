# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=255, verbose_name='Tipo')),
                ('valor', models.CharField(max_length=255, verbose_name='Contenido')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
    ]
