from . import views
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [

    path('', views.index, name = 'index' ),
    path('login', views.log_in, name = 'log_in' ),
    path('logout', views.log_out, name = 'log_out'),
]

