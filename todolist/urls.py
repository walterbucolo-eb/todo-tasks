from django.conf.urls import include, url
from django.contrib import admin
from todolistapp.views import TaskLogin, TaskLogout

urlpatterns = [
    url(r'^account/login/$', TaskLogin.as_view(), name='login'),
    url(r'^account/$', TaskLogout.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'events/', include('todolistapp.urls')),
    url('', include('social_django.urls', namespace='social')),
    url('', TaskLogin.as_view(), name='login'),
]
