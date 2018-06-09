### django
#### 项目的创建
* 切到虚拟环境: django-admin startproject projectname
* 创建应用: python manage.py startapp appname
#### 配置debug
* Django 仅在调试模式下（DEBUG=True）能对外提供静态文件
* 当 DEBUG=False 工作在生产模式时，Django不再对外提供静态文件
#### 静态文件配置
* 静态文件访问字段:STATIC_URL = '/static/'
* 静态文件根根目录:STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#### url配置
* 2.0中好处是避免数据类型转换,可以不用多定义url,定义多个正则匹配
##### django2.0前:  
参数默认中是字符串,字段必须和视图中参数一致:url(r'index/(?P<category>\d+)/(?P<page>\d+)$', views.index),
##### django2.0后:
2.0中可以指定对应的参数类型:path('index/<int:category>/<int:page>/', views.index),
