# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0011_auto_20170922_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='year_in_school',
            field=models.CharField(choices=[('ТАРИФ1', 'ТАРИФ1'), ('ТАРИФ2', 'ТАРИФ2'), ('ТАРИФ3', 'ТАРИФ3')], default='ТАРИФ1', max_length=2),
        ),
    ]
