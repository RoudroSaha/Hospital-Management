from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='doctors_home'),
    path('list/', views.doctor_list, name='doctor_list'),
]