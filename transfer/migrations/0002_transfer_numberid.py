# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='numberid',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
