# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0018_auto_20141112_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 5, 32, 25, 386904, tzinfo=utc), verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 5, 32, 25, 381400, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=128, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True),
            preserve_default=True,
        ),
    ]
