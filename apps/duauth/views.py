#coding:utf8

from django.shortcuts import render
from django.views.generic import View

# def login_view(request):
#     if request.method == 'GET':
#         return render(request,'auth/login.html')

class LoginView(View):
    def get(self,request):
        return render(request,'auth/login.html')