#coding:utf8

from django.urls import path
from . import views

app_name = 'payinfo'

urlpatterns = [
    path('',views.paytinfo,name='payinfo'),
]