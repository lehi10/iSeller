# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0010_auto_20171127_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='info',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(max_length=50),
        ),
    ]