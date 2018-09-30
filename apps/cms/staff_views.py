#coding:utf8
from django.shortcuts import render
from apps.duauth.models import User
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.models import Group
from django.shortcuts import redirect,reverse
from apps.duauth.decorators import du_superuser_required
from django.utils.decorators import method_decorator

@du_superuser_required
def staffs(request):
    context = {
        'staffs': User.objects.filter(Q(is_staff=True)|Q(is_superuser=True))
    }
    return render(request,'cms/staffs.html',context=context)

@method_decorator(du_superuser_required,name='dispatch')
class AddStaffView(View):
    def get(self,request):
        context = {
            'groups': Group.objects.all()
        }
        return render(request,'cms/add_staff.html',context=context)

    def post(self,request):
        telephone = request.POST.get('telephone')
        user = User.objects.get(telephone=telephone)
        user.is_staff = True
        groups_ids = request.POST.getlist('groups')
        groups = Group.objects.filter(pk__in=groups_ids)
        user.groups.set(groups)
        user.save()
        return redirect(reverse("cms:staffs"))
