#coding:utf8

from rest_framework import serializers
from .models import News,NewsCategory,Comment
from apps.duauth.serializers import UserSerializer

class NewsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsCategory
        fields = ('id','name')

class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer()
    author = UserSerializer()
    class Meta:
        model = News
        fields = ('id','title','desc','thumbnail','pub_time','category','author')

class CommentSerilizer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id','content','author','pub_time')