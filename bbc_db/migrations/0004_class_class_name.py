# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-17 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbc_db', '0003_remove_class_class_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_name',
            field=models.CharField(blank=True, db_column='CLASS_NAME', max_length=45, null=True),
        ),
    ]
