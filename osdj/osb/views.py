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
	#获取用户最喜欢的三个话题
	topics_list = Topics.objects.\
			annotate(num_likeduser=Count('likeduser')).\
			order_by('-num_likeduser')[0:8]
	recent_user_list = User.objects.order_by('-id')[0:7]
	return render(request, 'osb/index.html', locals())
