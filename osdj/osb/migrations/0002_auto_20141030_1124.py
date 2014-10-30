# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': '\u5c0f\u7ec4'},
        ),
        migrations.AlterModelOptions(
            name='topics',
            options={'verbose_name_plural': '\u8bdd\u9898'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AddField(
            model_name='topics',
            name='creator',
            field=models.ForeignKey(default=1, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to='osb.User'),
            preserve_default=False,
        ),
    ]
