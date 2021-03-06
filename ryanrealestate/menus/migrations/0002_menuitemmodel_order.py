# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitemmodel',
            name='order',
            field=models.IntegerField(default=0, help_text='The order of the menu items. e.g. Set to 0 for first, 100 for last.', verbose_name='Item Index'),
            preserve_default=False,
        ),
    ]
