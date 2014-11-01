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
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group as SysGroup
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from osb.models import User, Group, Topics, Comment

class UserCreationForm(forms.ModelForm):
	'''A form for creating new users. Includes all the 
	required fields,plus a repeated password.'''
	password1 = forms.CharField(label='密码', 
		widget=forms.PasswordInput)
	password2 = forms.CharField( label='密码验证', 
		widget=forms.PasswordInput)
	class Mate:
		model = User
		fields = ('username', 'email')

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('确保两次输入的密码相同')
		return password2

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
	password = forms.CharField(label='密码')
	
	class Mate:
		model = User
		fields = ('username', 'email', 'password', 'is_active', 'is_admin')

	def clean_password(self):
		return self.initial['password']

class OsbUserAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('username', 'email', 'is_admin')
	fieldsets = (
			(None, {'fields':('username', 'email', 'password')}),
			('详细信息', {'fields':('truename', 'nowcity', 'sex', 'birthday', 
				'telphone', 'picture', 'soldiercity', 'joindate',)}),
			('权限', {'fields':('is_admin',)}),
			#('重要事件', {'fields':('last_login')}),
	)

	add_fieldsets = (
		(None,{
			'classes':('wide',),	
			'fields': ('username', 'email', 'password1', 'password2')}
		),
	)

	list_filter = ('is_admin',)
	search_fileds = ('username',)
	ordering = ('username',)
	filter_horizontal = ()

admin.site.register(User, OsbUserAdmin)
admin.site.register(Group)
admin.site.register(Topics)
admin.site.register(Comment)
admin.site.unregister(SysGroup)
