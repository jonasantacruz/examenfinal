# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('isbn', models.IntegerField(max_length=13)),
                ('author', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=200)),
                ('editorial', models.CharField(max_length=40)),
                ('pais', models.CharField(max_length=40)),
                ('anio', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
