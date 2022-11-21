from django import views
from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('',views.login),
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('register',views.register),
    path('login', views.login),
    path('home',views.home),
    path('logout',views.logout_user),
]
