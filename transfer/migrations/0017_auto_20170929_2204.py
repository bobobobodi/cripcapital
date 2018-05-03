# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0016_auto_20170922_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='year_in_school',
            field=models.CharField(default='Standart', max_length=2, choices=[('Standart', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')]),
        ),
    ]
