#encoding: utf-8
from django import forms
from django.shortcuts import resolve_url, get_object_or_404
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView

from blog.models import Blog, Post
from comment.models import Comment


class BlogDetail(DetailView):
    template_name = "blog/blog_detail.html"
    model = Blog


class BlogList(ListView):
    template_name = "blog/blog_list.html"
    model = Blog


class PostDetail(CreateView):
    model = Comment
    template_name = 'post/post_detail.html'
    fields = ('text', )

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        return context

    def form_valid(self, form):
        if self.request.user.is_anonymous:
            raise forms.ValidationError(u'Вы не можете опубликовать комментарий, пока не войдете в учетную запись')
        form.instance.author = self.request.user
        form.instance.post = self.postobject
        return super(PostDetail, self).form_valid(form)

    def get_success_url(self):
        return resolve_url("blog:post_detail", pk=self.postobject.pk)


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'blog')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(editor=user)


class PostCreate(CreateView):
    form_class = PostCreateForm
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(PostCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return resolve_url("blog:post_detail", pk=self.object.pk)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class PostUpdate(UpdateView):
    form_class = PostUpdateForm
    template_name = 'post/post_update.html'
    model = Post

    def get_success_url(self):
        return resolve_url("blog:post_detail", pk=self.object.pk)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'categories')


class BlogCreate(CreateView):
    form_class = BlogForm
    template_name = 'blog/blog_create.html'

    def form_valid(self, form):
        form.instance.editor = self.request.user
        return super(BlogCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url("blog:blog_detail", pk=self.object.pk)


class BlogUpdate(UpdateView):
    template_name = 'blog/blog_update.html'
    form_class = BlogForm
    model = Blog

    def get_success_url(self):
        return resolve_url("blog:post_detail", pk=self.object.pk)
