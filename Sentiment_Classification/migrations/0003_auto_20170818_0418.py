# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sentiment_Classification', '0002_tweets'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='created_date',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='sentiment',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='tweets',
            name='tweet_text',
            field=models.TextField(max_length=250),
        ),
    ]
