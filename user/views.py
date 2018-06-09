import json

from django.http import HttpResponse, QueryDict

# Create your views here.
from django.shortcuts import render

from user.logutils import Log


def index(request, category, page):
    """
    显示首页
    @param request:
    @param category:
    @param page:
    @return:
    """
    Log.error("index", "sb")
    c = category + page
    return HttpResponse("Hello, world!_index %d" % c)


def testparam(request):
    """
    显示登录
    :param request:
    :return:
    """

    # ERROR: root:zhang__testparam__
    # {'name': ['jasamha', 'zsh'], 'id': ['3']}
    Log.error("testparam", dict(request.GET.lists()))
    # ERROR: root:zhang__testparam__
    # {'name': 'zsh', 'id': '3'}
    one = request.GET
    print(dict(one.lists()))
    Log.error("testparam", request.GET.dict())

    return HttpResponse("Hello, world!_login")


def show_image(request):
    """
    显示图片
    :param request:
    :return:
    """
    Log.error("showimage", "sb")
    return render(request, "index.html")


def testrequest(request):
    Log.error("method", request.method)
    Log.error("body", request.body.decode())
    Log.error("post_body", request.POST.dict())
    Log.error("post_body_json", json.dumps(request.POST.dict()))
    Log.error("token", request.META.get("HTTP_TOKEN"))
    Log.error("meta", request.META)
    Log.error("path", request.path)
    Log.error("path_info", request.path_info)
    return HttpResponse(json.dumps(request.POST.dict()))
