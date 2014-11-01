# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0011_auto_20141101_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
