# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0018_auto_20170929_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='year_in_school',
            field=models.CharField(default='Standart', choices=[('Standart', 'Standert'), ('Normal', 'Normal'), ('Premium', 'Premium'), ('Platinum', 'Platinum')], max_length=10),
        ),
    ]
