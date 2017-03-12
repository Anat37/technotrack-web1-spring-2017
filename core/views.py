from django.shortcuts import render
from django.views.generic.base import TemplateView

from blog.models import Blog
from comment.models import Comment
from post.models import Post


class HomePageView(TemplateView):
    template_name = "core/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blogs_cnt'] = Blog.objects.all().count()
        context['posts_cnt'] = Post.objects.all().count()
        context['comments_cnt'] = Comment.objects.all().count()
        return context
