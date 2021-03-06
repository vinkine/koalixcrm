# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-22 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_auto_20180119_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['position_number'], 'verbose_name': 'Position', 'verbose_name_plural': 'Positions'},
        ),
        migrations.AddField(
            model_name='salesdocument',
            name='custom_date_field',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Custom Date/Time'),
        ),
    ]
