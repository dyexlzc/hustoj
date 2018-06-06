# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-19 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0027_resource_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooc.Week', verbose_name='所属周次'),
        ),
    ]
