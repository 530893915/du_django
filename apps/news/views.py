from django.shortcuts import render
from .models import News,NewsCategory
from django.views.decorators.http import require_GET
from django.conf import settings
from  utils import restful
from .serializers import NewsSerializer

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
    start = settings.NEWS_COUNT_ONE_PAGE*(page-1)
    end =start + settings.NEWS_COUNT_ONE_PAGE
    newses = News.objects.all()[start:end]
    serializer = NewsSerializer(newses,many=True)
    return restful.result(data=serializer.data)


def news_detail(request,news_id):
    return render(request,'news/news_detail.html')

def search(request):
    return render(request,'news/search.html')