# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-17 13:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbc_db', '0002_class_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='class_name',
        ),
    ]
