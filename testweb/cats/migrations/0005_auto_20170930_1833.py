# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_auto_20170930_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='height',
            field=models.FloatField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adorable_kitten',
            name='height',
            field=models.FloatField(default=0, max_length=100),
        ),
    ]
