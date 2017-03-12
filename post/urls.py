# coding; utf-8
from django.conf.urls import url
from post.views import PostView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name="post_detail")
]
