# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0004_producto_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
