from django.db import models
from shortuuidfield import ShortUUIDField



class Payinfo(models.Model):
    price = models.FloatField()
    path = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)

class PayinfoOrder(models.Model):
    uid = ShortUUIDField(primary_key=True)
    payinfo = models.ForeignKey('Payinfo',on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    buyer = models.ForeignKey('duauth.User',on_delete=models.DO_NOTHING)
    pub_time = models.DateTimeField(auto_now_add=True)
    istype = models.SmallIntegerField(default=0)
    status = models.SmallIntegerField(default=1)