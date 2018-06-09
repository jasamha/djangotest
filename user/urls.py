"""
 *  @ 创建者      zsh
 *  @ 创建时间    18-6-8 下午4:50
 *  @ 创建描述    
 *  
"""
from django.conf.urls import url
from django.urls import path

from user import views

urlpatterns = [
    # url(r'index/(?P<category>\d+)/(?P<page>\d+)$', views.index),
    path('index/<int:category>/<int:page>/', views.index),
    path('testparam', views.testparam),
    path('showimage/', views.show_image),
    path('testrequest/', views.testrequest)
]
