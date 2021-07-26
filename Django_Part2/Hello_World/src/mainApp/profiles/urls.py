from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('<int:pk>/details/', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('confirmDelete/', views.confirmed, name='confirmed'),
    path('addProfile/', views.addProfile, name='addProfile'),
]