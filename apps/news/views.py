from django.shortcuts import render
from .models import News,NewsCategory,Comment
from django.views.decorators.http import require_GET,require_POST
from django.conf import settings
from  utils import restful
from .serializers import NewsSerializer,CommentSerilizer
from .forms import AddCommentForm
from apps.duauth.decorators import du_login_required

def index(request):
    newses = News.objects.select_related('category','author')[
        0:settings.NEWS_COUNT_ONE_PAGE
    ]
    categories = NewsCategory.objects.all()
    context = {
        'newses': newses,
        'categories': categories
    }
    return render(request,'news/index.html',context=context)

# 加载更多
@require_GET
def news_list(request):
    page = int(request.GET.get('p',1))
    category_id = int(request.GET.get('category_id',0))
    start = settings.NEWS_COUNT_ONE_PAGE*(page-1)
    end =start + settings.NEWS_COUNT_ONE_PAGE
    if category_id == 0:
        newses = News.objects.all()[start:end]
    else:
        newses = News.objects.filter(category_id=category_id)[start:end]
    serializer = NewsSerializer(newses,many=True)
    return restful.result(data=serializer.data)


def news_detail(request,news_id):
    try:
        news = News.objects.select_related('category', 'author').get(pk=news_id)
        context = {
            'news': news
        }
        return render(request, 'news/news_detail.html', context=context)
    except News.DoesNotExist:
        return render(request,'news/news_404.html')

# 评论
@du_login_required
@require_POST
def add_comment(request):
    form = AddCommentForm(request.POST)
    if form.is_valid():
        content = form.cleaned_data.get('content')
        news_id = form.cleaned_data.get('news_id')
        news = News.objects.get(pk=news_id)
        comment = Comment.objects.create(content=content,news=news,author=request.user)
        serilizer = CommentSerilizer(comment)
        return restful.result(data=serilizer.data)
    else:
        return restful.params_error(message=form.get_error())


def search(request):
    return render(request,'news/search.html')