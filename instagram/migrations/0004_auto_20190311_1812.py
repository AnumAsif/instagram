# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-11 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
