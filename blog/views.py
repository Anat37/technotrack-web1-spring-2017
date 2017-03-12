from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from blog.models import Blog


class BlogView(DetailView):
    template_name = "blog/blog_detail.html"
    model = Blog


class BlogList(ListView):
    template_name = "blog/blog_list.html"
    model = Blog
