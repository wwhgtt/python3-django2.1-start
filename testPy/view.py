# from django.http import HttpResponse
# Django 具有“视图”的概念，用于封装负责处理用户请求及返回响应的逻辑
 # django.shortcuts（快捷函数）
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'test'
    # render结合一个给定的模板hello.html和一个给定的上下文字典context 并返回一个渲染后的 HttpResponse 对象
    return render(request, 'hello.html', context)
    #  这里替换成base.html后展示的和hello.html中是不一样的  简单猜测一下此处如果是hello.html 因为hello.html继承了base 所以展示出的是base+hello
