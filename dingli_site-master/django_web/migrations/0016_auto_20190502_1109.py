# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-02 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0015_auto_20181114_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(blank=True, verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='extratitle',
            field=models.CharField(default='', max_length=16, verbose_name='\u989d\u5916\u804c\u4f4d'),
        ),
    ]
