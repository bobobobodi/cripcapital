# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0006_hz'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hz',
        ),
    ]
