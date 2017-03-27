# coding; utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from blog.views import BlogList, BlogDetail, PostDetail, PostUpdate, PostCreate, BlogCreate, BlogUpdate

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^post/(?P<pk>\d+)/$', PostDetail.as_view(), name="post_detail"),
    url(r'^post/update/(?P<pk>\d+)/$', login_required(PostUpdate.as_view()), name="post_update"),
    url(r'^post/create/$', login_required(PostCreate.as_view()), name="post_create"),
    url(r'^update/(?P<pk>\d+)/$', login_required(BlogUpdate.as_view()), name="blog_update"),
    url(r'^create/$', login_required(BlogCreate.as_view()), name="blog_create"),
]
