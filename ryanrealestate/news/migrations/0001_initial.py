# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 06:53
from __future__ import unicode_literals

import config.mixins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsIndexModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='This is the title that will be displayed on the page', max_length=120, verbose_name='Blog Index Page Title')),
                ('slug', models.SlugField(help_text='This is the blog index page as displayed in the URL.', max_length=120, verbose_name='Blog Index Page Slug')),
                ('meta_title', models.CharField(help_text='Important for SEO. Include keywords.', max_length=120, verbose_name='Page Meta Title')),
                ('meta_description', models.CharField(help_text='Important for SEO. Include keywords.', max_length=255, verbose_name='Page Meta Description')),
                ('description', models.TextField(blank=True, help_text='This will appear at the top of the page.', verbose_name='Page Description')),
            ],
            options={
                'verbose_name_plural': 'Blog Index Page Settings',
                'verbose_name': 'Blog Index Page Settings',
            },
            bases=(config.mixins.SingleInstanceMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NewsPostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title as it appears on the page.', max_length=255, verbose_name='Post Title')),
                ('slug', models.SlugField()),
                ('published', models.DateTimeField(auto_now=True, help_text='The date and time the post will go live.', verbose_name='Publish Date')),
                ('featured_image', models.ImageField(blank=True, help_text='Main Image for the post.', upload_to='img/news/%Y/%m', verbose_name='Featured Image')),
                ('body', models.TextField(blank=True, help_text='The main content of the post. HTML OK.', verbose_name='Post Body')),
                ('author', models.ForeignKey(help_text='The user who authored the post.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name_plural': 'News Posts',
                'verbose_name': 'News Post',
            },
        ),
    ]
