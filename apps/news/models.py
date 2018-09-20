from django.db import models

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)

# 新闻
class News(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    thumbnail = models.URLField()
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('NewsCategory',on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey('duauth.User',on_delete=models.SET_NULL,null=True)

    class Meta:
        ordering = ['-pub_time']

# 评论
class Comment(models.Model):
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey("News",on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey("duauth.User",on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_time']


# 轮播图
class Banner(models.Model):
    title_h3 = models.CharField(max_length=20)
    title_p = models.CharField(max_length=40)
    image_url = models.URLField()
    priority = models.IntegerField(default=0)
    link_to = models.URLField()
    pub_time = models.DateTimeField(auto_now_add=True)
