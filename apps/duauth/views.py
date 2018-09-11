#coding:utf8

from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from utils.captcha.hycaptcha import Captcha
from io import BytesIO
from django.http import HttpResponse

class LoginView(View):
    def get(self,request):
        return render(request,'auth/login.html')

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request,username=telephone,password=password)
            if user:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return redirect(reverse('news:index'))
            else:
                messages.info(request,'用户名或密码错误！')
                return redirect(reverse('duauth:login'))
        else:
            messages.info(request,'表单验证失败！')
            return redirect(reverse('duauth:login'))

class RegisterView(View):
    def get(self,request):
        return render(request, 'auth/register.html')

    def post(self,request):
        pass


def img_captcha(request):
    text,image = Captcha.gene_code()
    out = BytesIO()
    image.save(out,'png')
    out.seek(0)
    response = HttpResponse(content_type='image/png')
    response.write(out.read())
    response['Content-length'] = out.tell()
    return response
