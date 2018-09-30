#coding:utf8

from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from utils.captcha.hycaptcha import Captcha
from io import BytesIO
from django.http import HttpResponse
from utils.aliyunsdk import aliyun
from .models import User
from utils import restful

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

# Form表单版本的注册代码
# class RegisterView(View):
#     def get(self,request):
#         return render(request, 'auth/register.html')
#
#     def post(self,request):
#         form = RegisterForm(request.POST)
#         if form.is_valid() and form.validate_data(request):
#             telephone = form.cleaned_data.get('telephone')
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = User.objects.create_user(telephone=telephone,username=username,password=password)
#             login(request,user)
#             return redirect(reverse('news:index'))
#         else:
#             message = form.get_error()
#             messages.info(request,message)
#             return redirect(reverse('duauth:register'))

# ajax请求版本的注册代码
class RegisterView(View):
    def get(self,request):
        return render(request,'auth/register.html')

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid() and form.validate_data(request):
            # 先验证数据是否是合法的
            telephone = form.cleaned_data.get('telephone')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(telephone=telephone,username=username,password=password)
            login(request,user)
            return restful.ok()
        else:
            message = form.get_error()
            return restful.params_error(message=message)


# 注销登录
def logout_view(request):
    logout(request)
    return redirect(reverse('duauth:login'))

def img_captcha(request):
    text,image = Captcha.gene_code()
    out = BytesIO()
    image.save(out,'png')
    out.seek(0)
    response = HttpResponse(content_type='image/png')
    response.write(out.read())
    response['Content-length'] = out.tell()

    request.session['img_captcha'] = text

    return response

def sms_captcha(request):
    code = Captcha.gene_number()
    telephone = request.GET.get('telephone')

    request.session['sms_captcha'] = code

    # result = aliyun.send_sms(telephone,code=code)
    print(code)
    return HttpResponse('success')