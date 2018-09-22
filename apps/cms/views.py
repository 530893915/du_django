from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View
from django.views.decorators.http import require_POST,require_GET
from apps.news.models import NewsCategory,News,Banner
from utils import restful
from .forms import EditNewsCategoryForm,WriteNewsForm,AddBannerForm,EditBannerForm
from django.conf import settings
import os
import qiniu
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

@staff_member_required(login_url='/')
def index(request):
    return render(request,'cms/index.html')

# 新闻列表管理页面
def news_list(request):
    page = int(request.GET.get('p',1))
    newses = News.objects.select_related('category','author').all()
    paginator = Paginator(newses,5)
    page_obj = paginator.page(page)
    context = {
        'categories': NewsCategory.objects.all(),
        'newses': page_obj.object_list,
        'paginator': paginator,
        'page_obj': page_obj
    }
    return render(request,'cms/news_list.html',context=context)

# 发布新闻
@method_decorator(login_required(login_url='/account/login/'),name='dispatch')
class WriteNewsView(View):
    def get(self,request):
        context = {
            'categories':NewsCategory.objects.all()
        }
        return render(request,'cms/write_news.html',context=context)

    def post(self,request):
        form = WriteNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            category = NewsCategory.objects.get(pk=category_id)
            News.objects.create(title=title,desc=desc,thumbnail=thumbnail,content=content,category=category,author=request.user)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_error())

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

# 轮播图
def banners(request):
    return render(request,'cms/banners.html')

def banner_list(request):
    banners = list(Banner.objects.all().values())
    return restful.result(data={"banners":banners})

# 删除轮播图
def delete_banner(request):
    banner_id = request.POST.get('banner_id')
    banner = Banner.objects.filter(pk=banner_id).delete()
    return restful.ok()

# 编辑轮播图
def edit_banner(request):
    form = EditBannerForm(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get('pk')
        title_h3 = form.cleaned_data.get('title_h3')
        title_p = form.cleaned_data.get('title_p')
        image_url = form.cleaned_data.get('image_url')
        link_to = form.cleaned_data.get('link_to')
        priority = form.cleaned_data.get('priority')
        banner = Banner.objects.filter(pk=pk).update(title_h3=title_h3,title_p=title_p,image_url=image_url,link_to=link_to,priority=priority)
        return restful.ok()
    else:
        return restful.params_error(message=form.get_error())


# 上传轮播图
def add_banner(request):
    form = AddBannerForm(request.POST)
    if form.is_valid():
        title_h3 = form.cleaned_data.get('title_h3')
        title_p = form.cleaned_data.get('title_p')
        image_url = form.cleaned_data.get('image_url')
        link_to = form.cleaned_data.get('link_to')
        priority = form.cleaned_data.get('priority')
        banner = Banner.objects.create(title_h3=title_h3,title_p=title_p,image_url=image_url,link_to=link_to,priority=priority)
        return restful.result(data={"banner_id": banner.pk})
    else:
        return restful.params_error(message=form.get_error())

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