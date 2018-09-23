#coding:utf8
from django.views.generic import View
from django.shortcuts import render

class PubCourse(View):
    def get(self,request):
        return render(request,'cms/pub_course.html')

    def post(self,request):
        pass