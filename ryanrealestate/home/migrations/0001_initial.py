# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 19:15
from __future__ import unicode_literals

import config.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(help_text='The Page title as it appears on the page', max_length=120, verbose_name='Homepage Title')),
                ('meta_title', models.CharField(help_text='Very important for SEO. Include keywords.', max_length=120, verbose_name='Homepage Meta Title')),
                ('meta_description', models.CharField(help_text='Very important for SEO. Include keywords.', max_length=255, verbose_name='Homepage Meta Description')),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name': 'Homepage Settings',
                'verbose_name_plural': 'Homepage Settings',
            },
            bases=(config.mixins.SingleInstanceMixin, models.Model),
        ),
    ]
