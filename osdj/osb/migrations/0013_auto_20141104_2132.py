# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0012_auto_20141101_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=128, verbose_name=b'\xe8\x81\x8a\xe5\xa4\xa9\xe5\x86\x85\xe5\xae\xb9')),
                ('createtime', models.DateTimeField(default=datetime.datetime(2014, 11, 4, 13, 32, 6, 584195, tzinfo=utc), verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe6\x97\xb6\xe9\x97\xb4')),
                ('fromuser', models.ForeignKey(related_name='sender', verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe6\x96\xb9', to=settings.AUTH_USER_MODEL)),
                ('touser', models.ForeignKey(related_name='receiver', verbose_name=b'\xe6\x8e\xa5\xe6\x94\xb6\xe6\x96\xb9', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='father',
            field=models.ForeignKey(verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe8\xaf\x84\xe8\xae\xba', blank=True, to='osb.Comment', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topics',
            name='createdate',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 4, 13, 32, 6, 578574, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
