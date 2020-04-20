from django.contrib import admin
from django.urls import path
from basic_app import views
from register import views as views_2

app_name = 'basic_app'

urlpatterns = [
    path('', views.index , name='index'),
    path('login', views.user_login , name='login'),
    path('register', views.user_register , name='register'),
   
]
