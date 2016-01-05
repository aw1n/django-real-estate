# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspostmodel',
            name='meta_description',
            field=models.CharField(default='', help_text='Important for SEO. Include keywords', max_length=255, verbose_name='Meta Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newspostmodel',
            name='meta_title',
            field=models.CharField(default='', help_text='Important for SEO. Include Keywords.', max_length=120, verbose_name='Meta Title'),
            preserve_default=False,
        ),
    ]