from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View
from django.views.decorators.http import require_POST,require_GET
from apps.news.models import NewsCategory
from utils import restful
from .forms import EditNewsCategoryForm
from django.conf import settings
import os
import qiniu

@staff_member_required(login_url='/')
def index(request):
    return render(request,'cms/index.html')

# 发布新闻
class WriteNewsView(View):
    def get(self,request):
        context = {
            'categories':NewsCategory.objects.all()
        }
        return render(request,'cms/write_news.html',context=context)

    def post(self,request):
        pass

# 新闻分类
def news_category(request):
    categories = NewsCategory.objects.order_by('-id')
    context = {
        'categories':categories
    }
    return render(request,'cms/news_category.html',context=context)

# 添加分类
@require_POST
def add_news_category(request):
    name = request.POST.get('name')
    exists = NewsCategory.objects.filter(name=name).exists()
    if not exists:
        NewsCategory.objects.create(name=name)
        return restful.ok()
    else:
        return restful.params_error(message='该分类已存在！')

# 修改分类
@require_POST
def edit_news_category(request):
    form = EditNewsCategoryForm(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get('pk')
        name = form.cleaned_data.get('name')
        try:
            NewsCategory.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error(message='这个分类不存在！')
    else:
        return restful.params_error(message=form.get_error())


# 删除分类
@require_POST
def delete_news_category(request):
    pk = request.POST.get('pk')
    try:
        NewsCategory.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.params_error(message='该分类不存在！')

# 发布新闻-七牛云上传文件
@require_GET
def qntoken(request):
    access_key = 'SXJAGOM6nPxMAInwr3y5yy8cuGdQeIHIKsyMsvqt'
    secret_key = 'uoYTDGLeAbrzEcQRhuRyYhB_In8RF2ageTqE7QK4'
    q = qiniu.Auth(access_key,secret_key)
    bucket = 'dubbs'
    token = q.upload_token(bucket)
    return restful.result(data={'token':token})

# 上传文件到自己的服务器
@require_POST
def upload_file(request):
    file = request.FILES.get('upfile')
    if not file:
        return restful.params_error(message='没有上传任何文件！')
    name = file.name # C:/User/meida/a.jpg
    filepath = os.path.join(settings.MEDIA_ROOT,name)
    with open(filepath,'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    # /media/0.jpg
    # http://127.0.0.1:8000/media/0.jpg
    url = request.build_absolute_uri(settings.MEDIA_URL+name)
    return restful.result(data={"url":url})