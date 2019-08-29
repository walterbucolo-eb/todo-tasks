from django.conf.urls import url
from . import views

urlpatterns = [
    # url('tasks/create/', views.TaskCreate.as_view(), name='task-create'),
    url('tasks/update/(?P<pk>[0-9]+)/$', views.TaskUpdate.as_view(), name='event-task-update'),
    url('tasks/delete/(?P<pk>[0-9]+)/$', views.TaskDelete.as_view(), name='event-task-delete'),
    url('(?P<event_id>[0-9]+)/tasks/$', views.TaskList.as_view(), name='task-list'),
    url('(?P<event_id>[0-9]+)/task/create/$', views.TaskCreate.as_view(), name='event-task-create'),
    url('', views.EventTask.as_view(), name='event-list'),
]
