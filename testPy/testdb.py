# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
    test1 = Test(name='root')
    test1.save()
    return HttpResponse("<p>test</p>")

    # HttpResponse是view.py中render最终返回  可以直接在页面中展示
