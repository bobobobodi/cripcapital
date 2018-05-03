# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0007_delete_hz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='numberid',
        ),
    ]
