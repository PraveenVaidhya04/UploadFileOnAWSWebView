from django.urls import path
from . import views
from django.contrib.auth import views as auth_login

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),

]