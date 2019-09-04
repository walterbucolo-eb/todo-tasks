from django.test import TestCase
from todolistapp.models import Task, Priority
from datetime import datetime
from django.contrib.auth.models import User


class PriorityTestCase(TestCase):
    def setUp(self):
        Priority.objects.create(priority='URGENT')
        Priority.objects.create(priority='NORMAL')
        Priority.objects.create(priority='LOW')

    def test_priority_urgent(self):
        priority_urgent = Priority.objects.get(priority='URGENT')
        self.assertEqual(priority_urgent.priority, 'URGENT')

    def test_priority_normal(self):
        priority_normal = Priority.objects.get(priority='NORMAL')
        self.assertEqual(priority_normal.priority, 'NORMAL')

    def test_priority_low(self):
        priority_low = Priority.objects.get(priority='LOW')
        self.assertEqual(priority_low.priority, 'LOW')


class TaskTestCase(TestCase):
    def setUp(self):
        self.priority = Priority.objects.create(priority='URGENT')
        # import ipdb; ipdb.set_trace()
        date = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
        user_test = User.objects.create_user('test', password='Test1')
        user_test.is_superuser = True
        user_test.is_staff = True
        user_test.save()
        self.task = Task.objects.create(
            name="Do task", done=False, date_task=date, user=user_test, priority=self.priority, event="012837")

    def test_task_response(self):
        # task = Task.objects.get(pk=1)
        response = 'Name: {}, Done: {}, User: {}, Priority: {}'.format(
            'Do task',
            False,
            'test',
            'URGENT')
        self.assertEqual(self.task.__str__(), response)
        
    

    