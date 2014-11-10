# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0016_auto_20141106_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 10, 52, 23, 606513, tzinfo=utc), verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 10, 52, 23, 603328, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default=b'default.jpg', upload_to=b'userImages', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
            preserve_default=True,
        ),
    ]
