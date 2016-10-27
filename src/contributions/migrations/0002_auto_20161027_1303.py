# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-27 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dustbin',
            name='name',
            field=models.CharField(default='cool', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dustbin',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dustbin'),
        ),
        migrations.AlterField(
            model_name='waste',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='waste'),
        ),
    ]
