# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingmodel',
            name='date_sold',
            field=models.DateField(blank=True, help_text='The date the property was sold', null=True, verbose_name='Date Sold'),
        ),
    ]
