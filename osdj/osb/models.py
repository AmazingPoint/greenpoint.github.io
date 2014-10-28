##############################
#FileName	: models.py
#Location	: app_olb(应用——olb)
#CreateDate	: 2014-10-28
#Author		: AmzingPoint
##############################

from django.db import models

class User(models.Model):
	'''The information for user, 用户基本信息'''
	username = models.CharField('用户名', max_length=16)
	password = models.CharField('密码', max_length=32)
	truename = models.CharField('真名', max_length=32)
	nowcity = models.CharField('现居城市', max_length=42)
	soldiercity = models.CharField('服役地点', max_length=42)
	joindate = models.Datefield('入伍年份')
	email = models.EmailField('邮箱')
	sex = models.BooleanField('性别') 
	state = models.BooleanField('当前状态')
	birthday = models.Datefield('生日')
	telphone = models.CharField('电话')
	picture = models.ImageField('头像')

class Group(models.Model):
	'''The grop table one group have one leader who comes 
	from user, A group and be join with users
	小组表，一个小组只能有一个组长，与组长为多对一关系
	小组同时可以被多个用户加入, 小组与组员为一对多关系'''
	name = models.CharField('小组名称', max_length=32)
	leader = models.ForeignKey(User)
	member = models.ManyToOneRel(User)
	createdate = models.DateTimeField('创建时间')
	description = models.CharField('描述', max_length=360)
	image = models.ImageField('展示图片')

class Topics(models.Model):
	'''The topics must pub in a group and users can give 
	a heart, the realation-ship from topics to group is 
	many2One and with users who like it is one2many
	一个话题必须发布在一个小组里，用户可以给话题点赞，话题和
	小组之间是多对一关系，和点赞的用户之间时一对多关系'''
	headline = models.CharField('话题标题', max_length=128)
	description = models.CharFiled('话题描述', max_length=512)
	group = models.ForeignKey(Group)
	likeduser = models.ManyToOneRel(User)
	createdate = models.DateTimeField('创建时间')

class  comments(models.Model):
	'''Comment have a type and a id'''

	
