from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *
# Create your views here.

menu = [
    {'title': 'Works'},
    {'title': 'Blog'},
    {'title': 'Contact'},
]

class IndexPage(TemplateView):
    posts = Posts.objects.all()[:2]
    new_work = NewWork.objects.all()

    template_name = 'index/posts.html'
    extra_context = {
        'title': 'MyBlog',
        'menu': menu,
        'posts': posts,
        'work': new_work
    }
