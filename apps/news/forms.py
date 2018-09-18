#coding:utf8

from django import forms
from apps.forms import FormMixin

class AddCommentForm(forms.Form,FormMixin):
    content = forms.CharField()
    news_id = forms.IntegerField()