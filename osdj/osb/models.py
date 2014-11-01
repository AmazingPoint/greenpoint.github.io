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
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class OsbUserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if not email:
			raise ValueError('请填写您的邮箱')
		user = self.model(				           
			username=username,
			email=OsbUserManager.normalize_email(email),
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password=None):
		user = self.create_user(username, email, password)
		user.is_admin = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	'''The information for user, 用户基本信息'''
	username = models.CharField('用户名', max_length=48, unique=True)
#	password = models.CharField('密码', max_length=128)
	truename = models.CharField('真名', max_length=32, null=True, blank=True)
	nowcity = models.CharField('现居城市', max_length=42, null=True, blank=True)
	soldiercity = models.CharField('服役地点', max_length=42, null=True, blank=True)
	joindate = models.DateField('入伍年份', null=True, blank=True)
	email = models.EmailField('邮箱', max_length=128, unique=True)
	sex = models.CharField('性别', max_length=4, null=True, blank=True)
	state = models.BooleanField('当前状态', default=False)
	birthday = models.DateField('生日', null=True, blank=True)
	telphone = models.CharField('电话', max_length=14, null=True, blank=True)
	picture = models.ImageField('头像', upload_to='userImages', null=True, blank=True)
	is_admin = models.BooleanField(default=False)
	objects = OsbUserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ('email',)
	@property
	def is_staff(self):
		return self.is_admin
	def has_perm(self, perm, obj=None):
		return True
	def has_module_perms(self, app_label):
		return True
	def get_full_name(self):
		return self.username
	def get_short_name(self):
		return self.username
	def __unicode__(self):
		return self.username

	class Meta:
		verbose_name_plural = '用户'

class Group(models.Model):
	'''The grop table one group have one leader who comes 
	from user, A group and be join with users
	小组表，一个小组只能有一个组长，小组与组长为一对多关系
	小组同时可以被多个用户加入, 小组与用户为多对多关系'''
	name = models.CharField('小组名称', max_length=32)
	leader = models.ForeignKey(User, verbose_name='组长')
	member = models.ManyToManyField(User, related_name='groupmemberuser', null=True, blank=True)
	createdate = models.DateTimeField('创建时间', null=True, blank=True)
	description = models.CharField('描述', max_length=360)
	image = models.ImageField('展示图片', upload_to='groupImages', null=True, blank=True)
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = '小组'

class Topics(models.Model):
	'''The topics must pub in a group and users can give 
	a heart, the realation-ship from topics to group is 
	many2One and with users who like it is one2many
	一个话题必须发布在一个小组里，用户可以给话题点赞，话题和
	小组之间是多对一关系，和点赞的用户之间时多对多关系'''
	headline = models.CharField('话题标题', max_length=128)
	description = models.CharField('话题描述', max_length=512)
	group = models.ForeignKey(Group, verbose_name='所属小组' )
	creator = models.ForeignKey(User, verbose_name='创建者')
	likeduser = models.ManyToManyField(User, verbose_name='喜欢的人',  related_name='likegroupuser', null=True, blank=True)
	createdate = models.DateTimeField('创建时间', null=True, blank=True)
	def __unicode__(self):
		return self.headline

	class Meta:
		verbose_name_plural = '话题'

class  Comment(models.Model):
	'''Comments have a id that which topics be commented
	a pice of comment can also be liked by other user
	评论表，一条评论对应一个话题，和话题为多对一关系
	一个用户可以多次评论，评论与用户为多对多关系
	评论还可以被用户点赞，此时评论与点赞用户为一对多关系'''
	content = models.CharField('评论内容', max_length=1024)
	topics = models.ForeignKey(Topics)
	commenter = models.ForeignKey(User, verbose_name='评论者', related_name='commentcommentuser')
	likeduser = models.ManyToManyField(User, verbose_name='喜欢的用户', related_name='likecommentsuser')
	createdate = models.DateTimeField('评论时间')
	reply = models.ForeignKey('self', null=True, blank=True,verbose_name='回复')
	def __unicode__(self):
		return self.content[0:10]
	class Meta:
		verbose_name_plural = '评论'
