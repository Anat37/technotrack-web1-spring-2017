from django.shortcuts import render
from django.views.generic import DetailView

from post.models import Post


class PostView(DetailView):
    template_name = "post/post_detail.html"
    model = Post
