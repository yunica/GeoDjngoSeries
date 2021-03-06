# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 17:24
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Primer', '0002_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lineas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('ubicacion', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Multipunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('ubicacion', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
    ]
