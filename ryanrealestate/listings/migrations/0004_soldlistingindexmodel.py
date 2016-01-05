# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 16:39
from __future__ import unicode_literals

import config.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listingindexmodel_page_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldListingIndexModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(help_text='The displayed title of the Listing Index Page', max_length=120, verbose_name='Listing Index Page Title')),
                ('slug', models.SlugField(help_text='Listing Index Page Title as it appears in the url', max_length=120, verbose_name='Listing Index Page Slug')),
                ('meta_title', models.CharField(help_text='Very important for SEO. Include Keywords', max_length=120, verbose_name='Listing Index page Meta Title')),
                ('meta_description', models.CharField(help_text='Very important for SEO. Include keywords', max_length=255, verbose_name='Listing Index Page Meta Description')),
                ('page_description', models.TextField(blank=True, help_text='Describe the sold listings. HTML ok.', verbose_name='Page Description')),
                ('order_by', models.CharField(choices=[('date_available', 'Date Available'), ('date_published', 'Date Posted'), ('price', 'Listing Price')], default='date_available', max_length=120, verbose_name='Order Listings By')),
            ],
            options={
                'verbose_name_plural': 'Sold Listing Index Page Settings',
                'verbose_name': 'Sold Listing Index Page Settings',
            },
            bases=(config.mixins.SingleInstanceMixin, models.Model),
        ),
    ]
