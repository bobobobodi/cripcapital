# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0014_transfer_year_in_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='year_in_school',
            field=models.CharField(choices=[('TARIF1', 'TARIF1'), ('TARIF2', 'TARIF2'), ('TARIF3', 'TARIF3'), ('TARIF4', 'TARIF4')], max_length=2, default='TARIF1'),
        ),
    ]
