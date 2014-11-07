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
from django.http import HttpResponse
from django.core import serializers

def index(request):
	'''获取用户最喜欢的8个话题
	get 7 top topics'''
	top_topics_list = Topics.objects.\
			annotate(num_likeduser=Count('likeduser')).\
			order_by('-num_likeduser')[0:8]
	'''获取最新加入的7个用户
	get 7 new user'''
	recent_user_list = User.objects.order_by('-id')[0:7]
	'''获取成员最多的7个小组
	get 7 group which have more member'''
	top_group_list = Group.objects.\
			annotate(num_member=Count('member')).\
			order_by('-num_member')[0:7]
	return render(request, 'osb/index.html', locals())

def chat(request):
	'''获取朋友列表
	get friendlist'''
	user = request.user
	friend_list = user.following.filter(following=user)
	print(friend_list)
	return render(request, 'osb/chat.html', locals())

def sendMessage(request, userid):
	'''发送信息到服务器
	send message to server'''
	fu = request.user
	tu = User.objects.get(pk=userid)
	msg = request.GET['message']
	cm = ChatMessage(fromuser=fu, touser=tu, message=msg)
	cm.save()
	return HttpResponse("success")

def getMessage(request, fuserid):
	'''从服务器获取最新的未读消息
	get new unread  message '''
	touser = request.user
	fuser = User.objects.get(pk=fuserid)
	message = ChatMessage.objects.filter(touser=touser).filter(fromuser=fuser).filter(is_read=False).order_by('id')
	print(message)
	data = serializers.serialize("json", message)
	return HttpResponse(data, content_type='application/json')


def setMessageReaded(request, messageid):
	message = ChatMessage.objects.get(pk=messageid)
	message.is_read = True
	message.save()
	return True
