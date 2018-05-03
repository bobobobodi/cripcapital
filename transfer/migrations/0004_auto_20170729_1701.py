# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_auto_20170729_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='numberid',
            field=models.CharField(default=models.ForeignKey(to=settings.AUTH_USER_MODEL), max_length=200),
        ),
    ]
