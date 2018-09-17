#coding:utf8

from django.urls import path
from . import views
from django.shortcuts import reverse

app_name = 'news'

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<news_id>/',views.news_detail,name='news_detail'),
    path('search/',views.search,name='search'),
    path('list/',views.news_list,name='news_list'),
]