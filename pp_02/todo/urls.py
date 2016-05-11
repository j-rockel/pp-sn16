from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo_list$', views.todo_list, name='todo_list'),
    url(r'^todo_edit$', views.todo_edit, name='todo_edit'),
    url(r'^todo_add$', views.todo_add, name='todo_add'),
    url(r'^todo_impr$', views.todo_impr, name='todo_impr'),
]