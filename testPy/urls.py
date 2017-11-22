from django.conf.urls import *
from . import view, testdb, search, search2
from django.contrib import admin

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^admin/', admin.site.urls),
]
