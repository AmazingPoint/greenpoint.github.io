# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
###############################
#FileName	: models.py
#Location	: app_olb(应用——olb)
#CreateDate	: 2014-10-28
#Author		: AmzingPoint
###############################

from django.db import models

class User(models.Model):
	'''The information for user, 用户基本信息'''
	username = models.CharField('用户名', max_length=16)
	password = models.CharField('密码', max_length=32)
	truename = models.CharField('真名', max_length=32)
	nowcity = models.CharField('现居城市', max_length=42)
	soldiercity = models.CharField('服役地点', max_length=42)
	joindate = models.DateField('入伍年份')
	email = models.EmailField('邮箱')
	sex = models.CharField('性别', max_length=4)
	state = models.BooleanField('当前状态', default=False)
	birthday = models.DateField('生日')
	telphone = models.CharField('电话', max_length=14)
	picture = models.ImageField('头像')

class Group(models.Model):
	'''The grop table one group have one leader who comes 
	from user, A group and be join with users
	小组表，一个小组只能有一个组长，小组与组长为一对多关系
	小组同时可以被多个用户加入, 小组与用户为多对多关系'''
	name = models.CharField('小组名称', max_length=32)
	leader = models.ForeignKey(User)
	member = models.ManyToManyField(User, related_name='groupmemberuser')
	createdate = models.DateTimeField('创建时间')
	description = models.CharField('描述', max_length=360)
	image = models.ImageField('展示图片')

class Topics(models.Model):
	'''The topics must pub in a group and users can give 
	a heart, the realation-ship from topics to group is 
	many2One and with users who like it is one2many
	一个话题必须发布在一个小组里，用户可以给话题点赞，话题和
	小组之间是多对一关系，和点赞的用户之间时多对多关系'''
	headline = models.CharField('话题标题', max_length=128)
	description = models.CharField('话题描述', max_length=512)
	group = models.ForeignKey(Group)
	likeduser = models.ManyToManyField(User, related_name='likegroupuser')
	createdate = models.DateTimeField('创建时间')

class  Comments(models.Model):
	'''Comments have a id that which topics be commented
	a pice of comment can also be liked by other user
	评论表，一条评论对应一个话题，和话题为多对一关系
	一个用户可以多次评论，评论与用户为多对多关系
	评论还可以被用户点赞，此时评论与点赞用户为一对多关系'''
	content = models.CharField('评论内容', max_length=1024)
	topics = models.ForeignKey(Topics)
	commenter = models.ManyToManyField(User, related_name='commentcommentuser')
	likeduser = models.ManyToManyField(User, related_name='likecommentsuser')
	createdate = models.DateTimeField('评论时间')
	reply = models.ForeignKey('self')

