# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0009_transfer_money_off'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='year_in_school',
            field=models.CharField(default='FR', max_length=2, choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')]),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='date_off',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
