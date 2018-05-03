# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0017_auto_20170929_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='year_in_school',
            field=models.CharField(choices=[('Standart', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='Standart', max_length=10),
        ),
    ]
