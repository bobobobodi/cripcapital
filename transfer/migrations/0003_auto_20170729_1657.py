# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0002_transfer_numberid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='numberid',
            field=models.CharField(max_length=200, default='auth.User'),
        ),
    ]
