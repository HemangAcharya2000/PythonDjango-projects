from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('register',views.register,name='register'),
    path('contact',views.contact,name='contact'),
    path('info',views.info,name='info'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]