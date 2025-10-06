# inventory/urls.py
from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('create/', views.inventory_create, name='inventory_create'),
    path('update/<int:pk>/', views.inventory_update, name='inventory_update'),
    path('delete/<int:pk>/', views.inventory_delete, name='inventory_delete'),
]