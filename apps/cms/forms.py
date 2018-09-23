#coding:utf8

from apps.forms import FormMixin
from django import forms
from apps.news.models import News,Banner
from apps.course.models import Course

class EditNewsCategoryForm(forms.Form,FormMixin):
    pk = forms.IntegerField(error_messages={'required':'必须传入分类id'})
    name = forms.CharField(max_length=100,min_length=1)


class WriteNewsForm(forms.ModelForm,FormMixin):
    category = forms.IntegerField()
    class Meta:
        model = News
        fields = ('title','desc','thumbnail','content')
        error_messages = {
            'category': {
                'required': '必须传入分类的ID！'
            },
            'title' :{
                'required': '必须输入标题！',
            }
        }

class EditNewsForm(WriteNewsForm):
    pk = forms.IntegerField()

class AddBannerForm(forms.ModelForm,FormMixin):
    class Meta:
        model = Banner
        fields = ('title_h3','title_p','image_url','link_to','priority')

class EditBannerForm(forms.ModelForm,FormMixin):
    pk = forms.IntegerField()
    class Meta:
        model = Banner
        fields = ('title_h3','title_p','image_url','link_to','priority')

class AddCourseForm(forms.ModelForm,FormMixin):
    category_id = forms.IntegerField()
    teacher_id = forms.IntegerField()
    class Meta:
        model = Course
        exclude = ('pub_time','category','teacher')