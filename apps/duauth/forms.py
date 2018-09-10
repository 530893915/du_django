#coding:utf8

from django import forms

class LoginForm(forms.Form):
    telephone = forms.CharField(max_length=11,min_length=11,error_messages={'required':'必须输入手机号码！','min_length':'手机号码个数必须为11位！','max_length':'手机号码个数必须为11位！'})
    password = forms.CharField(min_length=6,max_length=20,error_messages={'required':'必须输入密码！','min_length':'密码最少不能小于6位！','max_length':'密码最多不能大于20位！'})
    remember = forms.IntegerField(required=False)
