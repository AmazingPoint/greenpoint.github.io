# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0009_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
