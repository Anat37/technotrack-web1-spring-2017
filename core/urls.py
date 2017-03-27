from django.conf.urls import url
from django.contrib.auth.views import login, logout

from core.views import HomePageView, CreateUser, RegisterSuc

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name="logout"),
    url(r'^register/', CreateUser.as_view(), name="register"),
    url(r'^register_success/', RegisterSuc.as_view(), name="register_success"),
]
