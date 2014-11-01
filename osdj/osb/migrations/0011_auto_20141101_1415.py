# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0010_remove_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=1024, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('createdate', models.DateTimeField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('commenter', models.ForeignKey(related_name='commentcommentuser', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
                ('likeduser', models.ManyToManyField(related_name='likecommentsuser', verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
                ('reply', models.ForeignKey(verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d', blank=True, to='osb.Comment', null=True)),
                ('topics', models.ForeignKey(to='osb.Topics')),
            ],
            options={
                'verbose_name_plural': '\u8bc4\u8bba',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comments',
            name='commenter',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='likeduser',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='topics',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
