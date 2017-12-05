# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0015_auto_20171127_1338'),
        ('dashboard', '0002_auto_20171128_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id_oferta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_oferta', models.CharField(max_length=50)),
                ('descripcion_oferta', models.CharField(max_length=300)),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Producto')),
            ],
        ),
        migrations.RemoveField(
            model_name='ofertamodel',
            name='producto',
        ),
        migrations.DeleteModel(
            name='ofertaModel',
        ),
    ]