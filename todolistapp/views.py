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
from django.shortcuts import redirect
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
        event_id = self.kwargs['event_id']
        # import ipdb ; ipdb.set_trace()
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
    fields = ['name', 'priority', 'date_task']

    def get_success_url(self):
        return reverse_lazy('task-list', kwargs=self.kwargs)

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        form.instance.event = self.kwargs['event_id']
        self.object = form.save()
        return super(TaskCreate, self).form_valid(form)

# def check_task(self, request, pk):
#     task = Task.objects.get(pk=pk)
#     if not task.done:
#         task.done = True
#     task.save()
#     return redirect('task-list')

class TaskUpdate(UpdateView):
    model = Task
    fields = ['name', 'done', 'priority']

    def get_success_url(self):
        return reverse_lazy('task-list', kwargs={'event_id': self.kwargs['event_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

    def get_success_url(self):
        return reverse_lazy('task-list', kwargs={'event_id': self.kwargs['event_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

