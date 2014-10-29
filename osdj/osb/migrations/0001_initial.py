# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=1024, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('createdate', models.DateTimeField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\xb0\x8f\xe7\xbb\x84\xe5\x90\x8d\xe7\xa7\xb0')),
                ('createdate', models.DateTimeField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('description', models.CharField(max_length=360, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=128, verbose_name=b'\xe8\xaf\x9d\xe9\xa2\x98\xe6\xa0\x87\xe9\xa2\x98')),
                ('description', models.CharField(max_length=512, verbose_name=b'\xe8\xaf\x9d\xe9\xa2\x98\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('createdate', models.DateTimeField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('group', models.ForeignKey(to='osb.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=16, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('truename', models.CharField(max_length=32, verbose_name=b'\xe7\x9c\x9f\xe5\x90\x8d')),
                ('nowcity', models.CharField(max_length=42, verbose_name=b'\xe7\x8e\xb0\xe5\xb1\x85\xe5\x9f\x8e\xe5\xb8\x82')),
                ('soldiercity', models.CharField(max_length=42, verbose_name=b'\xe6\x9c\x8d\xe5\xbd\xb9\xe5\x9c\xb0\xe7\x82\xb9')),
                ('joindate', models.DateField(verbose_name=b'\xe5\x85\xa5\xe4\xbc\x8d\xe5\xb9\xb4\xe4\xbb\xbd')),
                ('email', models.EmailField(max_length=75, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('sex', models.CharField(max_length=4, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('state', models.BooleanField(default=False, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81')),
                ('birthday', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5')),
                ('telphone', models.CharField(max_length=14, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('picture', models.ImageField(upload_to=b'', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='topics',
            name='likeduser',
            field=models.ManyToManyField(related_name='likegroupuser', to='osb.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(to='osb.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(related_name='groupmemberuser', to='osb.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='commenter',
            field=models.ManyToManyField(related_name='commentcommentuser', to='osb.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='likeduser',
            field=models.ManyToManyField(related_name='likecommentsuser', to='osb.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(to='osb.comments'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='topics',
            field=models.ForeignKey(to='osb.Topics'),
            preserve_default=True,
        ),
    ]
