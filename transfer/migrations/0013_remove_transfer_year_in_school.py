# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0012_auto_20170922_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='year_in_school',
        ),
    ]
