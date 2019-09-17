from django.conf.urls import url
from django.contrib.auth import views
from django.contrib.auth.views import login

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^login$', views.LoginView.as_view(), name='login'),
]
