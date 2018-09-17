#coding:utf8

from django import template
from datetime import datetime
from django.utils.timezone import now as now_func

register = template.Library()

@register.filter
def time_since(value,now=None, reversed=False):
    if not isinstance(value,datetime):
        return value

    now = now_func()
    timestamp = (now - value).total_seconds()
    if timestamp < 60:
        return '刚刚'
    elif 3600>timestamp>=60:
        minutes = int(timestamp//60)
        return '%s分钟前' % minutes
    elif 60*60*24>timestamp>=3600:
        hours = int(timestamp//3600)
        return '%s小时前' % hours
    elif 60*60*24*30>timestamp>=60*60*24:
        days = int(timestamp//60*60*24)
        return '%s天前' % days
    else:
        return value.strftime("%Y/%m/%d/%H:%M")