# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0007_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joindate',
            field=models.DateField(null=True, verbose_name=b'\xe5\x85\xa5\xe4\xbc\x8d\xe5\xb9\xb4\xe4\xbb\xbd', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='soldiercity',
            field=models.CharField(max_length=42, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\xbd\xb9\xe5\x9c\xb0\xe7\x82\xb9', blank=True),
            preserve_default=True,
        ),
    ]
