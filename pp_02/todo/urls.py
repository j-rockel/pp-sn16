from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^$', views.todo_edit, name='todo_edit'),
    url(r'^$', views.todo_add, name='todo_add'),
    url(r'^$', views.todo_impr, name='todo_impr'),
]