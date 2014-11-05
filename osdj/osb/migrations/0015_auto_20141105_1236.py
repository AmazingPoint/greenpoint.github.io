# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0014_auto_20141105_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 5, 4, 36, 45, 308077, tzinfo=utc), verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 5, 4, 36, 45, 304596, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
