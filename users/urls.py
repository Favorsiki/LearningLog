"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views
app_name = 'users'
urlpatterns = [
    #登录界面
    #url(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),
    url(r'^login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #用户界面注销
    url(r'logout/$', views.logout_view, name='logout'),
    #新用户注册
    url(r'^register/$', views.register, name='register'),
]