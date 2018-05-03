# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0004_auto_20170729_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='numberid',
            field=models.CharField(default='', max_length=200),
        ),
    ]
