# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0010_auto_20170922_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'ТАРИФ1'), ('SO', 'ТАРИФ2'), ('JR', 'ТАРИФ3')], max_length=2, default='FR'),
        ),
    ]
