# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0013_auto_20141104_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(db_constraint=b'\xe5\x85\xb3\xe6\xb3\xa8\xe7\x9a\x84\xe4\xba\xba', to=settings.AUTH_USER_MODEL, related_name='following_rel_+'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 5, 4, 35, 44, 785314, tzinfo=utc), verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 5, 4, 35, 44, 781975, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
