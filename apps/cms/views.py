from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View

@staff_member_required(login_url='/')
def index(request):
    return render(request,'cms/index.html')

class WriteNewsView(View):
    def get(self,request):
        return render(request,'cms/write_news.html')