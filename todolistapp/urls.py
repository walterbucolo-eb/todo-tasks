from django.conf.urls import url
from . import views

urlpatterns = [
    url('(?P<event_id>[0-9]+)/tasks/create/', views.TaskCreate.as_view(), name='event-task-create'),
    url('(?P<event_id>[0-9]+)/tasks/update/(?P<pk>[0-9]+)/$', views.TaskUpdate.as_view(), name='event-task-update'),
    url('(?P<event_id>[0-9]+)/tasks/delete/(?P<pk>[0-9]+)/$', views.TaskDelete.as_view(), name='event-task-delete'),
    url('(?P<event_id>[0-9]+)/tasks/$', views.TaskList.as_view(), name='task-list'),
    url('task/create/$', views.TaskCreate.as_view(), name='event-task-create'),
    url('', views.EventTask.as_view(), name='event-list'),
]
