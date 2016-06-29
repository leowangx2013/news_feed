# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subreddit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('subreddit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='subreddit.Subreddit')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]