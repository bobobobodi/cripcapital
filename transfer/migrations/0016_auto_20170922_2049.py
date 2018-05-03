# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0015_auto_20170922_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='year_in_school',
            field=models.CharField(default='FR', max_length=2, choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')]),
        ),
    ]
