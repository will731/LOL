# -*- coding: UTF-8 -*-
"""LOL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.auth.views import login
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^index/$', index),  # 首页
    url(r'^$', index, name='index'),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^get_username/$', get_username),  # 获取当前登陆用户名

    # 机器
    url(r'^cmdb/', include('cmdb.urls')),
    # 业务
    url(r'^business/', include('business.urls')),
    # 作业平台
    url(r'^job/', include('job.urls')),
    # 日志记录
    url(r'^log_record/', include('log_record.urls')),
]
