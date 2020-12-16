# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-12-15 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('-created_at',), 'verbose_name': 'employee', 'verbose_name_plural': 'employees'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_code',
            field=models.CharField(blank=True, max_length=60, unique=True),
        ),
    ]
