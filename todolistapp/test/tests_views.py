from django.test import Client
from django.test import TestCase
from todolistapp.models import Priority
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from datetime import datetime


class LoginTestCase(TestCase):
    def setUp(self):
        # self.priority = Priority.object.create(priority='URGENT')
        self.user = User.objects.create_user(username='testuser', password='12345')
        UserSocialAuth.objects.create(
            user=self.user,
            provider='eventbrite',
            uid='34563456',
            extra_data={
                'auth_time': 1567447106,
                'access_token': 'KLHJLJHLKJH',
                'token_type': 'bearer',
            }
        )

    def test_login_true(self):
        c = Client()
        response = c.post('/account/login/', {'username': 'testuser', 'password': '12345'})
        self.assertEqual(302, response.status_code)

    def test_login_false(self):
        c = Client()
        response = c.post('/account/login/', {'username': 'test2', 'password': 'Tevjhvst1'})
        self.assertEqual(200, response.status_code)

    def test_login_bad_request(self):
        c = Client()
        response = c.post('/aaccount/login/', {'username': 'test2', 'password': 'Tevjhvst1'})
        self.assertEqual(404, response.status_code)

    def test_create_task(self):
        c = Client()
        date = datetime.now()
        priority = Priority.objects.create(priority='URGENT')
        URL = "/events/{}/tasks/create/".format('68602296315')
        data = {'name': 'task', 'priority': priority, 'date_task': date}
        response = c.post(URL, data)
        import ipdb ; ipdb.set_trace()













# class CreateTaskCase(TestCase):
#     def setUp(self):
#         user_test = User.objects.create_user('test1', password='Test1')
#         user_test.is_superuser = True
#         user_test.is_staff = True
#         user_test.save()

#     def test_get_events(TestCase):
#         pass