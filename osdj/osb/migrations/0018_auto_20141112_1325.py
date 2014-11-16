# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0017_auto_20141110_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 5, 25, 48, 900377, tzinfo=utc), verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 5, 25, 48, 896913, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
