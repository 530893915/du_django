#coding:utf8

from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('',views.course_index,name='index'),
    path('detail/<course_id>/',views.course_detail,name='course_detail'),
]