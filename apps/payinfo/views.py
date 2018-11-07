from django.shortcuts import render
from .models import Payinfo,PayinfoOrder
from django.shortcuts import redirect,reverse
from django.views.decorators.csrf import csrf_exempt
from utils import restful
from hashlib import md5
from django.http import FileResponse
from apps.duauth.decorators import du_login_required
from django.conf import settings
import os

def index(request):
    payinfos = Payinfo.objects.all()
    context = {
        'payinfos': payinfos
    }
    return render(request,'payinfo/payinfo.html',context=context)

@du_login_required
def payinfo_order(request):
    payinfo_id = request.GET.get('payinfo_id')
    payinfo = Payinfo.objects.get(pk=payinfo_id)
    buyed = PayinfoOrder.objects.filter(buyer=request.user,payinfo=payinfo,status=2)
    if buyed:
        return redirect(reverse("payinfo:index"))

    order = PayinfoOrder.objects.create(buyer=request.user,amount=payinfo.price,payinfo=payinfo,status=1)
    context = {
        'payinfo': payinfo,
        'order': order,
        'notify_url': request.build_absolute_uri(reverse('payinfo:notify_view')),
        'return_url': request.build_absolute_uri(reverse('payinfo:download_payinfo')+"?payinfo_id=%s"%payinfo.pk)
    }
    return render(request,'payinfo/create_order.html',context=context)

@csrf_exempt
def notify_view(request):
    orderid = request.POST.get('orderid')
    PayinfoOrder.objects.filter(pk=orderid).update(status=2)
    return restful.ok()

def order_key(request):
    goodsname = request.POST.get("goodsname")
    istype = request.POST.get("istype")
    notify_url = request.POST.get("notify_url")
    orderid = request.POST.get("orderid")
    price = request.POST.get("price")
    return_url = request.POST.get("return_url")

    token = 'e6110f92abcb11040ba153967847b7a6'
    orderuid = str(request.user.pk)
    uid = '49dc532695baa99e16e01bc0'

    key = md5((goodsname + istype + notify_url + orderid + orderuid + price + return_url + token + uid).encode("utf-8")).hexdigest()
    # key = md5("".join([goodsname, istype, notify_url, orderuid, orderuid, price, return_url, token, uid]).encode(
    #     "utf-8")).hexdigest()
    return restful.result(data={'key': key})

def download_payinfo(request):
    payinfo_id = request.GET.get('payinfo_id')
    payinfo = Payinfo.objects.get(pk=payinfo_id)
    buyed = Payinfo.objects.filter(payinfo=payinfo,buyer=request.user,status=2)
    if not buyed:
        redirect(reverse('payinfo:index'))
    path = payinfo.path
    # 作为附件下载
    response = FileResponse(open(os.path.join(settings.MEDIA_ROOT,path),'rb'))
    response['Content-Type'] = 'image/jpeg'
    response['Content-Disposition'] = 'attachment;filename="%s"'%path.split("/")[-1]
    return response

