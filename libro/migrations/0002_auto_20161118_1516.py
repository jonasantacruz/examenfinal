# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='isbn',
            field=models.PositiveIntegerField(serialize=False, primary_key=True, validators=[django.core.validators.MaxValueValidator(9999999999999)]),
        ),
    ]
