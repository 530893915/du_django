#coding:utf8

from django.urls import path
from . import views
from django.shortcuts import reverse

app_name = 'news'

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<news_id>/',views.news_detail,name='detail'),
    path('search/',views.search,name='search'),
    path('list/',views.news_list,name='news_list'),
    path('add_comment/',views.add_comment,name='add_comment'),
]