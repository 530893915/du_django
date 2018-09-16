from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View
from django.views.decorators.http import require_POST
from apps.news.models import NewsCategory
from utils import restful
from .forms import EditNewsCategoryForm

@staff_member_required(login_url='/')
def index(request):
    return render(request,'cms/index.html')

class WriteNewsView(View):
    def get(self,request):
        return render(request,'cms/write_news.html')

    def post(self,request):
        pass

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