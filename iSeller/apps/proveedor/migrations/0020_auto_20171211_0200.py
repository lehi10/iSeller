# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0019_auto_20171210_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='urlImagen',
            field=models.ImageField(upload_to='productosImg/'),
        ),
    ]
