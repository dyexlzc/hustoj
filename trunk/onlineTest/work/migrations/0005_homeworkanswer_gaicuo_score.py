# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-16 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20170916_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworkanswer',
            name='gaicuo_score',
            field=models.IntegerField(default=0, verbose_name='程序改错题成绩'),
        ),
    ]
