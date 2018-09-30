#coding:utf8

from utils import restful
from django.shortcuts import redirect
from functools import wraps
from django.contrib.auth.models import Permission,ContentType
from django.http import Http404

def du_login_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            if request.is_ajax():
                return restful.unauth(message='请先登录！')
            else:
                return redirect('/')
    return wrapper

def du_permission_required(model):
    def decorator(viewfunc):
        @wraps(viewfunc)
        def _wrapper(request,*args,**kwargs):
            content_type = ContentType.objects.get_for_model(model)
            permissions = Permission.objects.filter(content_type=content_type)
            codenames = [content_type.app_label + "." + permission.codename for permission in permissions]

            # has_perms：只能采用字符串的形式判断
            # 字符串的形式为：app_label.codename
            result = request.user.has_perms(codenames)
            if result:
                return viewfunc(request,*args,**kwargs)
            else:
                raise Http404
        return _wrapper
    return decorator

def du_superuser_required(viewfunc):
    @wraps(viewfunc)
    def _wrapper(request,*args,**kwargs):
        if request.user.is_superuser:
            return viewfunc(request,*args,**kwargs)
        else:
            raise Http404()
    return _wrapper