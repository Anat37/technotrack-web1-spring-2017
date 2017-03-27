from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from blog.models import Blog, Post
from comment.models import Comment


class HomePageView(TemplateView):
    template_name = "core/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blogs_cnt'] = Blog.objects.all().count()
        context['posts_cnt'] = Post.objects.all().count()
        context['comments_cnt'] = Comment.objects.all().count()
        return context


class AppUserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class CreateUser(CreateView):
    form_class = AppUserCreateForm
    model = get_user_model()
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:register_success')


class RegisterSuc(TemplateView):
    template_name = "core/register_success.html"

