# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-17 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbc_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_name',
            field=models.CharField(db_column='CLASS_NAME', default='ClassName', max_length=45),
            preserve_default=False,
        ),
    ]
