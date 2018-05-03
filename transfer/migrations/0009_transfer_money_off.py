# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0008_remove_transfer_numberid'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='money_off',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
