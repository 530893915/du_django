#coding:utf8

from django import forms
from apps.forms import FormMixin

class AddCommentForm(forms.Form,FormMixin):
    content = forms.CharField(error_messages={'required': '评论不能为空！'})
    news_id = forms.IntegerField(error_messages={'required': '系统接收不到新闻id！'})