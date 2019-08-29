# from django.shortcuts import render
# from django.http import HttpResponse
# from material import LayoutMixin, Layout, Row
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import Task
from django.urls import (
    reverse_lazy
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from eventbrite import Eventbrite


class TaskLogin(LoginView):
    pass


class TaskLogout(LogoutView):
    template = '../TEMPLATES/registration/logout.html'


class TaskList(TemplateView, LoginRequiredMixin):
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        content_data = super(TaskList, self).get_context_data(**kwargs)
        content_data['list_tasks'] = Task.objects.filter(event=self.kwargs['event_id'])
        return content_data


class EventTask(TemplateView):
    template_name = "event.html"

    def get_events(self):
        social = self.request.user.social_auth.all()[0]
        token = social.access_token
        eventbrite = Eventbrite(token)
        list_events = eventbrite.get('/users/me/events/')['events']
        return list_events

    def get_context_data(self):
        content_data = super().get_context_data()
        content_data['list_events'] = self.get_events()
        return content_data


class TaskCreate(CreateView):
    model = Task
    fields = ['name', 'priority']
    success_url = reverse_lazy('event-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event = self.kwargs['event_id']
        self.object = form.save()
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    fields = ['name', 'done', 'priority']
    success_url = reverse_lazy('event-list')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('event-list')


# def get_token(user):
#     token = user.social_auth.get(
#         provider='eventbrite'
#     ).access_token
#     return token
