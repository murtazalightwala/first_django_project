from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('staff_registration/', views.staff_registration, name = 'staff_registration'),
        path('staff_registration/register_staff', views.register_staff, name = 'register_staff'),

]
