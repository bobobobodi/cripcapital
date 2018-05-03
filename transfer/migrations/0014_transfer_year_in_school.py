# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0013_remove_transfer_year_in_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='year_in_school',
            field=models.CharField(default='ТАРИФ1', max_length=2, choices=[('ТАРИФ1', 'ТАРИФ1'), ('ТАРИФ2', 'ТАРИФ2'), ('ТАРИФ3', 'ТАРИФ3')]),
        ),
    ]
