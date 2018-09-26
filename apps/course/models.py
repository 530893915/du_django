from django.db import models

class CourseCategory(models.Model):
    name = models.CharField(max_length=100)

class Teacer(models.Model):
    username = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    profile = models.TextField()
    avatar = models.URLField()

class Course(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    cover_url = models.URLField()
    price = models.FloatField()
    duration = models.IntegerField()
    profile = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('CourseCategory',on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey('Teacer',on_delete=models.DO_NOTHING)

class CourseOrder(models.Model):
    pub_time = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    status = models.SmallIntegerField()
    course = models.ForeignKey("Course",on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey("duauth.User",on_delete=models.DO_NOTHING)
    # 1:支付宝支付
    # 2:微信支付
    istype = models.SmallIntegerField()
