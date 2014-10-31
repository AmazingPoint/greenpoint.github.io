# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
###############################
#FileName	: models.py
#Location	: app_olb(应用——olb)
#CreateDate	: 2014-10-29
#Author		: AmzingPoint
###############################

from django.shortcuts import render
from osb.models import *
from django.db.models import Count

def index(request):
	#获取用户最喜欢的8个话题
	#get 7 top topics 
	top_topics_list = Topics.objects.\
			annotate(num_likeduser=Count('likeduser')).\
			order_by('-num_likeduser')[0:8]
	#获取最新加入的7个用户
	#get 7 new user
	recent_user_list = User.objects.order_by('-id')[0:7]
	#获取成员最多的7个小组
	#get 7 group which have more member
	top_group_list = Group.objects.\
			annotate(num_member=Count('member')).\
			order_by('-num_member')[0:7]
	return render(request, 'osb/index.html', locals())
