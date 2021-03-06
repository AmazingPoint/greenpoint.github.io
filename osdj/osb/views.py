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

from django.shortcuts import render, render_to_response
from osb.models import *
from django.contrib.auth import authenticate,login,hashers 
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.template.loader import get_template
from django.template import Context



def index(request):
	user = request.user
	if user.is_authenticated():
		return HttpResponseRedirect('/osb/home/'+user.username)
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

def home(request, username):
	'''用户主页
	user's own page'''
	user = request.user
	if(user.username == username):
		user_following_topics_list = Topics.objects.filter(creator = user.following.all())[0:30]
		user_group_list = Group.objects.filter(leader = user)
		user_added_group_list = Group.objects.filter(member = user)
		user_topics_list = Topics.objects.filter(creator=user)[0:30]
		return render(request, 'osb/home.html', locals())
	else:
		show_user = User.objects.get(username=username)
		user_group_list = Group.objects.filter(leader=show_user)
		user_topics_list = Topics.objects.filter(creator=show_user)[0:30]
		return render(request, 'osb/customer_home.html', locals())


#registry
def registration(request):
	'''用户注册
	user registration'''
	username = request.POST['username']
	password_unmake = request.POST['password1']
	password = hashers.make_password(password_unmake)
	new_user = User(username=username, password=password)
	new_user.save()
	user = authenticate(username=username, password=password_unmake)
	if user is not None:
		login(request,user)
		print(user)
		return HttpResponseRedirect('/osb/index')
	else:
		return HttpResponseRedirect('/osb/registry')

def registry(request):
	return render(request, 'osb/registry.html')

def profile(request):
	return render(request, 'osb/index.html')

def checkUsername(request, username):
	count = User.objects.filter(username=username).count()
	print("################################# %d",count)
	return HttpResponse(count)

#IM
def chat(request):
	'''获取朋友列表
	get friendlist'''
	user = request.user
	friend_list = user.following.filter(following=user)
	return render(request, 'osb/chat.html', locals())

def getFromuser(request):
	'''获取发送消息且消息没被读取的用户
	get the friend who sent message to you'''
	user = request.user
	messages = ChatMessage.objects.filter(touser=user).filter(is_read=False)
	message_list = list(messages)
	friend_list = []
	for message in message_list:
		if(message.fromuser not in friend_list):
			friend_list.append(message.fromuser)
	t = get_template('osb/chat_friend.html')
	html = t.render(Context({'unread_friend_list': friend_list }))
	return HttpResponse(html)

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
	data = serializers.serialize("json", message)
	return HttpResponse(data, content_type='application/json')

def setMessageReaded(request, messageid):
	'''设置消息状态为已读
	set the message is readed'''
	message = ChatMessage.objects.get(pk=messageid)
	message.is_read = True
	message.save()
	return True

def checkMessageNumber(request):
	'''从服务器获取未读消息的数量
	get the message number which not be readed'''
	user = request.user
	number = ChatMessage.objects.filter(touser=user).filter(is_read=False).count()
	print(number)
	return HttpResponse(number)
