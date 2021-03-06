# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0015_auto_20171127_1338'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ofertaModel',
            fields=[
                ('id_oferta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_oferta', models.CharField(max_length=50)),
                ('descripcion_oferta', models.CharField(max_length=300)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Producto')),
            ],
        ),
        migrations.DeleteModel(
            name='oferta',
        ),
    ]
