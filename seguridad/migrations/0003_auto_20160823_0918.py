# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0002_auto_20160822_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectosistema',
            name='id_proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='seguridad.Proyecto'),
        ),
        migrations.AlterField(
            model_name='proyectosistema',
            name='id_sistema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sistemas', to='seguridad.Sistema'),
        ),
    ]
