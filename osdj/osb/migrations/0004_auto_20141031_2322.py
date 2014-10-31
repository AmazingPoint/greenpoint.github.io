# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0003_auto_20141031_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=128, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, max_length=48, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d'),
            preserve_default=True,
        ),
    ]
