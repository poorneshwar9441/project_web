from django.contrib import admin
from django.urls import path,include
from .views import sign_in,login,login_render,home_page,data_render,add_todo,delete_todo


urlpatterns = [
    path('',home_page),
    path('signin',sign_in),
    path('login',login_render),
    path('loggingin',login),
    path('data/<str:name>/<str:password>',data_render),
    path('addtodo/<str:name>/<str:password>',add_todo),
    path('Delete/<str:name>/<str:password>/<str:id>',delete_todo)
]

