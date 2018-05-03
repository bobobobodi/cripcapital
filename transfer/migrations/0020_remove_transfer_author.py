# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0019_auto_20170929_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='author',
        ),
    ]
