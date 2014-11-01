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

from django.contrib import admin
from osb.models import User, Group, Topics, Comment

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Topics)
admin.site.register(Comment)
