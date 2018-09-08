#coding:utf8

from django.urls import path
from . import views
from django.shortcuts import reverse

app_name = 'news'

urlpatterns = [
    path('',views.index,name='index')
]