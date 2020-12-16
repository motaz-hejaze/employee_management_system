# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-12-16 19:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_system', '0002_auto_20201215_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_code',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Mobile Number length must be between 6 and 20 numbers', regex='^\\d{6,20}$')], verbose_name='Mobile Number'),
        ),
    ]