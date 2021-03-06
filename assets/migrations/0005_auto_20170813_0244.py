# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-13 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20170812_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='line',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AlterField(
            model_name='host',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(2, '已下线'), (1, '在线'), (4, '备用'), (3, '故障')], default=1, null=True, verbose_name='资产状态'),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(2, '已下线'), (1, '在线'), (4, '备用'), (3, '故障')], default=0, verbose_name='资产状态'),
        ),
        migrations.DeleteModel(
            name='Line',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
