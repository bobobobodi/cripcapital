# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0005_auto_20170729_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('hz', models.CharField(max_length=200)),
            ],
        ),
    ]
