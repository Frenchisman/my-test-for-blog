# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0004_auto_20160802_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Galerie', 'verbose_name_plural': 'Galeries'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Titre de la Galerie'),
        ),
    ]