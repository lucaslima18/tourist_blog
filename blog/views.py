from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostsList(ListView):
    queryset = Post.objects.filter(status='published')
    model = Post
    paginate_by = 20
    template_name = "posts_list.html"