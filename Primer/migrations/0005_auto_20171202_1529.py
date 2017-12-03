# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-02 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Primer', '0004_delitosmuni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='delitosmuni',
            name='idfalso',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='delitosmuni',
            name='nuevadireccion',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='delitosmuni',
            name='referenciado',
            field=models.BooleanField(default=False),
        ),
    ]
