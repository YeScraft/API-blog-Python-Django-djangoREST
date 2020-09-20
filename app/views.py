from django.shortcuts import render
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer, PostDetailSerializer
from rest_framework import generics, viewsets


# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('-title')
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all().order_by('-title')
    serializer_class = CategorySerializer
