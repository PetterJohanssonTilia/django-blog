from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    #model = Post
    #template_name = 'blog/post_list.html' #Used if we didnt name the model post_list.html
    queryset = Post.objects.filter(status=1)
    #queryset = Post.objects.all()
    #queryset = Post.objects.filter(author=2)