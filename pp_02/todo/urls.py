from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo_list$', views.todo_list, name='todo_list'),
    url(r'^todo/(?P<pk>\d+)/$', views.todo_edit, name='todo_edit'),
    url(r'^todo/new$', views.todo_add, name='todo_add'),
    url(r'^todo_impr$', views.todo_impr, name='todo_impr'),
    url(r'^todo/del/(?P<pk>\d+)/$', views.todo_del, name='todo_del'),
]