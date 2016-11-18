# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20161118_1516'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Libro',
        ),
    ]
