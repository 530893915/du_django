#coding:utf8

from django.urls import path
from . import views

app_name = 'duauth'

urlpatterns = [
    path("login/",views.LoginView.as_view(),name='login')
]