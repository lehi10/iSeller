# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20171227_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='permisos',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='tiempo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='user_destino',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
