from django.conf.urls import *
from . import view,testdb

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^testdb$', testdb.testdb),
]
