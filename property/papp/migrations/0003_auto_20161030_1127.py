# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-30 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import papp.models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0002_flat_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='image1',
            field=models.FileField(blank=True, null=True, verbose_name='\u0424\u043e\u0442\u043e 1'),
        ),
    ]